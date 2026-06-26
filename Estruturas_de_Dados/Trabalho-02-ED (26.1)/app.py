"""
app.py  –  Estruturas de Dados (TUI)
Requer: pip install textual
"""

from textual.app         import App, ComposeResult
from textual.binding     import Binding
from textual.containers  import Container, Horizontal, Vertical, ScrollableContainer, VerticalScroll
from textual.widgets     import (
    Header, Footer, Button, Input, Label, Select,
    Static, Log, TabbedContent, TabPane, Collapsible, Tree, SelectionList,
)
from textual.widgets.selection_list import Selection
from textual.reactive    import reactive
from textual             import on

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from exemplos.historico_web       import HistoricoWeb
from exemplos.fila_atendimento    import FilaAtendimento
from exemplos.gerenciador_tarefas import GerenciadorTarefas


# ═══════════════════════════════════════════════════════════════════════════ #
#  Aba: Pilha – Histórico Web  (Tree widget)                                  #
# ═══════════════════════════════════════════════════════════════════════════ #

class TabPilha(Static):

    backend: reactive[str] = reactive("array")

    def on_mount(self):
        self._historico = HistoricoWeb(self.backend)
        self._refresh_view()

    def watch_backend(self, value: str):
        if hasattr(self, '_historico'):
            self._historico = HistoricoWeb(value)
            self._refresh_view()

    def _bigo_text(self) -> str:
        if self.backend == 'array':
            return "Array  →  push O(1)*  |  pop O(1)  |  peek O(1)"
        return "LinkedList  →  push O(1)  |  pop O(1)  |  peek O(1)"

    def compose(self) -> ComposeResult:
        # controles no topo
        with Container(classes="controls"):
            yield Input(placeholder="URL  ex: https://github.com", id="pilha-input")
            with Horizontal(classes="btn-row"):
                yield Button("🌐 Visitar",  id="btn-visitar",     variant="success")
                yield Button("⬅  Voltar",   id="btn-voltar",      variant="warning")
                yield Button("🗑  Limpar",   id="btn-pilha-clear", variant="error")

        # big-O colapsável
        with Collapsible(title="Complexidade Big-O", id="coll-pilha", collapsed=True):
            yield Static(self._bigo_text(), id="bigo-pilha", classes="bigo-text")

        # visualização + log lado a lado
        with Horizontal(classes="tab-layout"):
            with VerticalScroll(classes="struct-box"):
                yield Label("📚 Histórico (topo → fundo)", classes="section-title")
                tree = Tree("🌐 Sessão atual", id="pilha-tree")
                tree.root.expand()
                yield tree
            with Vertical(classes="log-box"):
                yield Label("📋 Log de ações", classes="section-title")
                yield Log(id="pilha-log", max_lines=200)

    def _refresh_view(self):
        tree: Tree = self.query_one("#pilha-tree", Tree)
        tree.clear()
        tree.root.set_label("🌐 Sessão atual")
        historico = self._historico.historico()   # mais antigo → mais recente
        if not historico:
            tree.root.add_leaf("(vazio)")
            return
        # topo fica como primeiro filho destacado
        for i, url in enumerate(reversed(historico)):
            label = f"▶ {url}" if i == 0 else f"   {url}"
            node = tree.root.add_leaf(label)

    def _log(self, msg: str):
        self.query_one("#pilha-log", Log).write_line(msg)

    @on(Button.Pressed, "#btn-visitar")
    def visitar(self):
        url = self.query_one("#pilha-input", Input).value.strip()
        if not url:
            return
        self._log(self._historico.visitar(url))
        self.query_one("#pilha-input", Input).clear()
        self._refresh_view()

    @on(Button.Pressed, "#btn-voltar")
    def voltar(self):
        self._log(self._historico.voltar())
        self._refresh_view()

    @on(Button.Pressed, "#btn-pilha-clear")
    def limpar(self):
        self._historico.limpar()
        self._log("─── Histórico limpo ───")
        self._refresh_view()


# ═══════════════════════════════════════════════════════════════════════════ #
#  Aba: Fila – Atendimento  (cards visuais com cabeça/fim)                    #
# ═══════════════════════════════════════════════════════════════════════════ #

class FilaCard(Static):
    """Card visual de um cliente na fila."""
    DEFAULT_CSS = """
    FilaCard {
        height: auto;
        border: round $primary;
        padding: 0 1;
        margin: 0 0 1 0;
        color: $text;
    }
    FilaCard.head-card {
        border: heavy $success;
        color: $success;
        text-style: bold;
    }
    FilaCard.tail-card {
        border: round $warning;
        color: $warning;
    }
    """


class TabFila(Static):

    backend: reactive[str] = reactive("array")

    def on_mount(self):
        self._fila = FilaAtendimento(self.backend)
        self._refresh_view()

    def watch_backend(self, value: str):
        if hasattr(self, '_fila'):
            self._fila = FilaAtendimento(value)
            self._refresh_view()

    def _bigo_text(self) -> str:
        if self.backend == 'array':
            return "Array  →  enqueue O(1)*  |  dequeue O(n)"
        return "LinkedList  →  enqueue O(n)  |  dequeue O(1)"

    def compose(self) -> ComposeResult:
        # controles no topo
        with Container(classes="controls"):
            yield Input(placeholder="Nome do cliente  ex: João Silva", id="fila-input")
            with Horizontal(classes="btn-row"):
                yield Button("➕ Entrada",  id="btn-chegada",    variant="success")
                yield Button("✅ Atender",  id="btn-atender",    variant="warning")
                yield Button("🗑  Limpar",  id="btn-fila-clear", variant="error")

        # big-O colapsável
        with Collapsible(title="Complexidade Big-O", id="coll-fila", collapsed=True):
            yield Static(self._bigo_text(), id="bigo-fila", classes="bigo-text")

        # visualização + log lado a lado
        with Horizontal(classes="tab-layout"):
            with VerticalScroll(classes="struct-box", id="fila-cards-area"):
                yield Label("🪑 Fila de atendimento", classes="section-title")
                yield Label("◀ SAÍDA (atendido)          ENTRADA ▶", classes="fila-direcao")
                yield Static("(vazia)", id="fila-empty-msg", classes="struct-empty")
            with Vertical(classes="log-box"):
                yield Label("📋 Log de ações", classes="section-title")
                yield Log(id="fila-log", max_lines=200)

    def _refresh_view(self):
        area = self.query_one("#fila-cards-area", VerticalScroll)
        # remove cards antigos
        for card in area.query(FilaCard):
            card.remove()
        msg = self.query_one("#fila-empty-msg", Static)

        fila = self._fila.fila_atual()
        if not fila:
            msg.display = True
            return
        msg.display = False
        total = len(fila)
        for i, nome in enumerate(fila):
            if i == 0:
                texto = f"  ▶ [{i+1}] {nome}  ← CABEÇA (próximo a sair)"
                card  = FilaCard(texto, classes="head-card")
            elif i == total - 1:
                texto = f"  ◀ [{i+1}] {nome}  ← FIM da fila"
                card  = FilaCard(texto, classes="tail-card")
            else:
                texto = f"    [{i+1}] {nome}"
                card  = FilaCard(texto)
            area.mount(card)

    def _log(self, msg: str):
        self.query_one("#fila-log", Log).write_line(msg)

    @on(Button.Pressed, "#btn-chegada")
    def chegada(self):
        nome = self.query_one("#fila-input", Input).value.strip()
        if not nome:
            return
        self._log(self._fila.chegada(nome))
        self.query_one("#fila-input", Input).clear()
        self._refresh_view()

    @on(Button.Pressed, "#btn-atender")
    def atender(self):
        self._log(self._fila.atender())
        self._refresh_view()

    @on(Button.Pressed, "#btn-fila-clear")
    def limpar(self):
        self._fila.limpar()
        self._log("─── Fila limpa ───")
        self._refresh_view()


# ═══════════════════════════════════════════════════════════════════════════ #
#  Aba: Lista – Gerenciador de Tarefas  (SelectionList)                       #
# ═══════════════════════════════════════════════════════════════════════════ #

class TabLista(Static):

    backend: reactive[str] = reactive("array")

    def on_mount(self):
        self._gerenciador = GerenciadorTarefas(self.backend)
        self._refresh_view()

    def watch_backend(self, value: str):
        if hasattr(self, '_gerenciador'):
            self._gerenciador = GerenciadorTarefas(value)
            self._refresh_view()

    def _bigo_text(self) -> str:
        if self.backend == 'array':
            return "Array  →  add O(1)*  |  insert O(n)  |  remove O(n)  |  get O(1)"
        return "LinkedList  →  add O(n)  |  insert O(1)  |  remove O(n)  |  get O(n)"

    def compose(self) -> ComposeResult:
        # controles no topo
        with Container(classes="controls"):
            yield Input(placeholder="Nome da tarefa  ex: Estudar estruturas", id="lista-input")
            with Horizontal(classes="btn-row"):
                yield Button("➕ Adicionar",   id="btn-add-tarefa",  variant="success")
                yield Button("⚡ Prioritária", id="btn-prioritaria", variant="warning")
                yield Button("✅ Concluir sel.", id="btn-concluir",  variant="success")
                yield Button("🗑  Limpar",      id="btn-lista-clear", variant="error")

        # big-O colapsável
        with Collapsible(title="Complexidade Big-O", id="coll-lista", collapsed=True):
            yield Static(self._bigo_text(), id="bigo-lista", classes="bigo-text")

        # visualização + log lado a lado
        with Horizontal(classes="tab-layout"):
            with VerticalScroll(classes="struct-box"):
                yield Label("📝 Tarefas pendentes", classes="section-title")
                yield SelectionList(id="lista-selection")
            with Vertical(classes="log-box"):
                yield Label("📋 Log de ações", classes="section-title")
                yield Log(id="lista-log", max_lines=200)

    def _refresh_view(self):
        sl: SelectionList = self.query_one("#lista-selection", SelectionList)
        tarefas = self._gerenciador.tarefas()
        sl.clear_options()
        for i, t in enumerate(tarefas):
            sl.add_option(Selection(f"[{i+1}] {t}", t, initial_state=False))

    def _log(self, msg: str):
        self.query_one("#lista-log", Log).write_line(msg)

    @on(Button.Pressed, "#btn-add-tarefa")
    def adicionar(self):
        tarefa = self.query_one("#lista-input", Input).value.strip()
        if not tarefa:
            return
        self._log(self._gerenciador.adicionar(tarefa))
        self.query_one("#lista-input", Input).clear()
        self._refresh_view()

    @on(Button.Pressed, "#btn-prioritaria")
    def prioritaria(self):
        tarefa = self.query_one("#lista-input", Input).value.strip()
        if not tarefa:
            return
        self._log(self._gerenciador.prioritaria(tarefa))
        self.query_one("#lista-input", Input).clear()
        self._refresh_view()

    @on(Button.Pressed, "#btn-concluir")
    def concluir(self):
        sl: SelectionList = self.query_one("#lista-selection", SelectionList)
        selecionadas = list(sl.selected)
        if not selecionadas:
            # tenta pelo input se não há seleção
            tarefa = self.query_one("#lista-input", Input).value.strip()
            if tarefa:
                self._log(self._gerenciador.concluir(tarefa))
                self.query_one("#lista-input", Input).clear()
        else:
            for valor in selecionadas:
                self._log(self._gerenciador.concluir(str(valor)))
        self._refresh_view()

    @on(Button.Pressed, "#btn-lista-clear")
    def limpar(self):
        self._gerenciador.limpar()
        self._log("─── Lista limpa ───")
        self._refresh_view()


# ═══════════════════════════════════════════════════════════════════════════ #
#  App principal                                                               #
# ═══════════════════════════════════════════════════════════════════════════ #

class EstruturasApp(App):

    CSS_PATH = "style.tcss"

    TITLE    = "Trabalho da Unidade II - Exemplos"
    SUB_TITLE = "Pilha | Fila | Lista"

    BINDINGS = [
        Binding("1",      "switch_tab('pilha')", "Pilha",  show=True),
        Binding("2",      "switch_tab('fila')",  "Fila",   show=True),
        Binding("3",      "switch_tab('lista')", "Lista",  show=True),
        Binding("t",      "toggle_dark",         "Tema",   show=True),
        Binding("h",      "toggle_help",         "Ajuda",  show=True),
        Binding("escape", "quit",                "Sair",   show=True),
    ]

    _help_visible: reactive[bool] = reactive(False)
    backend:       reactive[str]  = reactive("array")

    def compose(self) -> ComposeResult:
        yield Header()

        # barra de backend: select à esq., descrição à dir.
        with Horizontal(id="backend-bar"):
            with Horizontal(id="backend-left"):
                yield Label("Backend:", id="backend-label")
                yield Select(
                    [("Array", "array"), ("LinkedList", "linkedlist")],
                    id="select-backend",
                    value="array",
                    allow_blank=False,
                )
            yield Static(
                "Troque o backend a qualquer momento.\n"
                "A estrutura é reiniciada ao trocar.",
                id="backend-desc",
            )

        # painel de ajuda (oculto por padrão)
        yield Static(
            "  1 / 2 / 3  →  trocar aba   |   t  →  alternar tema   |   h  →  esta ajuda   |   Esc  →  sair",
            id="help-bar",
        )

        # abas centralizadas
        with TabbedContent(id="tabs", initial="pilha"):
            with TabPane("📚 Pilha – Histórico Web", id="pilha"):
                yield TabPilha(id="tab-pilha")
            with TabPane("🪑 Fila – Atendimento", id="fila"):
                yield TabFila(id="tab-fila")
            with TabPane("📝 Lista – Tarefas", id="lista"):
                yield TabLista(id="tab-lista")

        yield Footer(show_command_palette=False)

    # ── eventos ──────────────────────────────────────────────────────────── #

    def on_mount(self):
        self.query_one("#help-bar").display = False

    @on(Select.Changed, "#select-backend")
    def backend_changed(self, event: Select.Changed):
        valor = str(event.value)
        self.backend = valor
        self.query_one("#tab-pilha", TabPilha).backend = valor
        self.query_one("#tab-fila",  TabFila ).backend = valor
        self.query_one("#tab-lista", TabLista).backend = valor

    def action_switch_tab(self, tab: str):
        self.query_one("#tabs", TabbedContent).active = tab

    def action_toggle_help(self):
        bar = self.query_one("#help-bar")
        bar.display = not bar.display


# ═══════════════════════════════════════════════════════════════════════════ #

if __name__ == "__main__":
    EstruturasApp().run()
