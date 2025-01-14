""" Stage View for Recital """
# __doc__ (Stage View Model file for little Recital app for testing
# Queues and Piles)
from pathlib import Path
from app.views.stage_logo import StageLogo


class StageView():
    """
    Class for Stage View Model

    Arguments:
    queues (class)

    Returns a orderer ramdom list from 3 optional modes.

    >>> stage = StageView()
    True

    TODO:
        -

    """

    _pit_list = []
    _queue_list = []

    def __init__(self, queues: list, lang: object) -> str:
        """
        Init Function

        Arguments:
        self
        queues (class)
        """

        self._pit_list = queues.pit_list
        self._queue_list = queues.queue_list
        self.lang = lang

    @property
    def pit_list(self) -> list:
        """
        Property Getter for pit list

        Arguments:
        self

        Returns getter of pit_list for data builder (list)

        >>> self.pit_list
        []

        TODO:
            -
        """
        return self._pit_list

    @pit_list.setter
    def pit_list(self, value: str) -> list:
        """
        Function Setter for pit list

        Arguments:
        self
        value (str)

        Returns setter for pit_list to select data builder (list)

        >>> stage = StageView()
        >>> stage.pit_list
        []

        TODO:
            -
        """
        self._pit_list = value

    @property
    def queue_list(self) -> list:
        """
        Property Getter for queue list

        Arguments:
        self

        Returns getter of pit_list for data builder (list)

        >>> self.queue_list
        []

        TODO:
            -
        """
        return self._queue_list

    @queue_list.setter
    def queue_list(self, value: str) -> list:
        """
        Function Setter for queue list

        Arguments:
        self
        value (str)

        Returns setter for queue_list to select data builder (list)

        >>> stage = StageView()
        >>> stage.queue_list
        []

        TODO:
            -
        """
        self._queue_list = value

    @property
    def get_stage(self) -> str:
        """
        Property to return stage view

        Arguments:
        self

        Return stage container view (str)

        TODO:
            -
        """
        try:
            screen_lines = []
            logo = StageLogo.get_logo(self.lang)

            screen_lines.append(''.join(logo).center(110))

            screen_lines.append(self.line_break().center(40))
            screen_lines.append(
                ''.join(self.get_queue_container('pit', 4)['top'][0:4]).center(110))  # noqa: E501
            screen_lines.append(self.line_break().center(40))
            screen_lines.append(''.join(self.get_queue_container(
                'pit', 4)['center'][0:4]).center(110))
            screen_lines.append(self.line_break().center(40))
            screen_lines.append(''.join(self.get_queue_container(
                'pit', 4)['bottom'][0:4]).center(110))

            screen_lines.append(self.line_break().center(60))

            screen_lines.append(
                ''.join(self.get_queue_container('pit', 4)['top'][4:]).center(60))  # noqa: E501
            screen_lines.append(self.line_break().center(60))
            screen_lines.append(
                ''.join(self.get_queue_container('pit', 4)['center'][4:]).center(60))  # noqa: E501
            screen_lines.append(self.line_break().center(60))
            screen_lines.append(
                ''.join(self.get_queue_container('pit', 4)['bottom'][4:]).center(60))  # noqa: E501

            screen_lines.append(self.line_break(3))

            screen_lines.append(
                ''.join(self.get_queue_container('queue')['top']))
            screen_lines.append(self.line_break())
            screen_lines.append(
                ''.join(self.get_queue_container('queue')['center']))
            screen_lines.append(self.line_break())
            screen_lines.append(
                ''.join(self.get_queue_container('queue')['bottom']))

            return ''.join(screen_lines)
        except TypeError as error:
            current_path = Path.cwd()
            txt_path = current_path/'app'/'static'/'txt'/'stage_logo.txt'
            print(
                self.lang["LANG"]["LANG_ERROR_READING_TXT"].format(txt_path),
                f'TypeError: {error}')
            return None

    def line_break(self, counter=1) -> str:
        """
        Function for line brake

        Arguments:
        self
        counter (int)

        Return line brakes by counter var (str)

        TODO:
            -
        """
        return '\n'*counter

    def get_queue_container(self, mode: str, split=0) -> list:
        """
        Function to return queue container view

        Arguments:
        self
        mode (str)
        split (int)

        Return queue container view data, returns a dict() (dict)

        TODO:
            -
        """
        if mode == 'pit':
            current_list = self._pit_list
        elif mode == 'queue':
            current_list = self._queue_list

        quehue_container = {}  # pylint: disable=C0200
        quehue_container['top'] = {}
        quehue_container['center'] = {}
        quehue_container['bottom'] = {}
        list_top = []
        list_center = []
        list_bottom = []

        for index in range(len(current_list)):  # pylint: disable=C0200
            counter = str(index+1)

            if index == 0:
                close_l = False
                close_r = True
                line_l = 0
                line_r = 0

            if index >= 1 and index <= len(current_list)-1:  # noqa: E501  # pylint: disable=R1716
                close_l = True
                close_r = True
                line_l = 1
                line_r = 0
                if split == index+1:
                    close_r = False
                    line_r = 0
                if split == index:
                    close_l = False
                    line_l = 0

            if index >= 9:
                close_l = False
                close_r = False
                line_l = 1
                line_r = 0

            qbox = self.get_queue_box(
                12, 3, counter+'|'+current_list[index],
                close_l, line_l, close_r, line_r)
            list_top.append(qbox['top'])
            list_center.append(qbox['center'])
            list_bottom.append(
                qbox['bottom'])

            quehue_container['top'] = list_top
            quehue_container['center'] = list_center
            quehue_container['bottom'] = list_bottom

        return quehue_container

    def get_queue_box(self, width: int, height: int, text: str,  # noqa: E501  # pylint: disable=R0913,R0914,R1710
                      close_l: bool, line_l: int, close_r: bool,
                      line_r: int) -> dict:
        """
        Function to return little queue box

        Arguments:
        self
        width (int)
        height (int)
        text (str)
        close_l (bool)
        line_l (int)
        close_r (bool)
        line_r (int)

        Return a little queue box, returns a dict() (dict)

        TODO:
            -
        """
        qbox_center = qbox_line_left = qbox_line_right = ''
        qbox_line_left_sp = qbox_line_right_sp = ''
        center_space = self.format_text(text, ' ' * (width))
        qbox_close_left = qbox_close_right = '│'

        if close_l:
            qbox_close_left = '┤'

        if close_r:
            qbox_close_right = '├'

        if line_l >= 1:
            qbox_line_left = '─'*line_l
            qbox_line_left_sp = ' '*line_l
            qbox_close_left = '┤'

        if line_r >= 1:
            qbox_line_right = '─'*line_r
            qbox_line_right_sp = ' '*line_r
            qbox_close_right = '├'

        # Special case: If the width or height is less than two, draw nothing:
        if width < 2 or height < 2:
            return

        # Print the top row:
        qbox_top = qbox_line_left_sp + '┌' + \
            ('─' * (width)) + '┐' + qbox_line_right_sp

        # Loop for center row (except the top and bottom):
        for _ in range(height - 2):
            # Print the sides:
            qbox_center = qbox_line_left+qbox_close_left + \
                center_space+qbox_close_right+qbox_line_right

        # Print the bottom row:
        qbox_bott = qbox_line_left_sp + '└' + \
            ('─' * (width)) + '┘' + qbox_line_right_sp

        return dict({'top': qbox_top, 'center': qbox_center,
                     'bottom': qbox_bott})

    def format_text(self, text: str, replacement: str) -> str:
        """
        Function to format the name spaces

        Arguments:
        self
        text (str)
        replacement (str)

        Return a fixed text limited by 12 chars (list)

        TODO:
            -
        """
        if len(text) > len(replacement):
            text = text[:12]

        return text.center(len(replacement))
