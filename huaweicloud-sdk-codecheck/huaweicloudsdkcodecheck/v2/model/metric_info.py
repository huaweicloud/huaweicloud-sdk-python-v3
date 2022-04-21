# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetricInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code_size': 'str',
        'raw_lines': 'str',
        'methods_total': 'str',
        'cyclomatic_complexity_total': 'str',
        'cyclomatic_complexity_per_method': 'str',
        'maximum_cyclomatic_complexity': 'str',
        'huge_cyclomatic_complexity_total': 'str',
        'huge_cyclomatic_complexity_ratio': 'str',
        'cca_cyclomatic_complexity_total': 'str',
        'cca_cyclomatic_complexity_per_method': 'str',
        'maximum_cca_cyclomatic_complexity': 'str',
        'huge_cca_cyclomatic_complexity_total': 'str',
        'cyclomatic_complexity_adequacy': 'str',
        'maximum_depth': 'str',
        'huge_depth_total': 'str',
        'huge_depth_ratio': 'str',
        'method_lines': 'str',
        'lines_per_method': 'str',
        'huge_method_total': 'str',
        'huge_method_ratio': 'str',
        'files_total': 'str',
        'folders_total': 'str',
        'lines_per_file': 'str',
        'huge_headerfile_total': 'str',
        'huge_headerfile_ratio': 'str',
        'huge_non_headerfile_total': 'str',
        'huge_non_headerfile_ratio': 'str',
        'huge_folder_total': 'str',
        'huge_folder_ratio': 'str',
        'file_duplication_total': 'str',
        'file_duplication_ratio': 'str',
        'non_hfile_duplication_total': 'str',
        'non_hfile_duplication_ratio': 'str',
        'code_duplication_total': 'str',
        'code_duplication_ratio': 'str',
        'non_hfile_code_duplication_total': 'str',
        'non_hfile_code_duplication_ratio': 'str',
        'unsafe_functions_total': 'str',
        'unsafe_functions_kloc': 'str',
        'redundant_code_total': 'str',
        'redundant_code_kloc': 'str',
        'warning_suppression_total': 'str',
        'warning_suppression_kloc': 'str'
    }

    attribute_map = {
        'code_size': 'code_size',
        'raw_lines': 'raw_lines',
        'methods_total': 'methods_total',
        'cyclomatic_complexity_total': 'cyclomatic_complexity_total',
        'cyclomatic_complexity_per_method': 'cyclomatic_complexity_per_method',
        'maximum_cyclomatic_complexity': 'maximum_cyclomatic_complexity',
        'huge_cyclomatic_complexity_total': 'huge_cyclomatic_complexity_total',
        'huge_cyclomatic_complexity_ratio': 'huge_cyclomatic_complexity_ratio',
        'cca_cyclomatic_complexity_total': 'cca_cyclomatic_complexity_total',
        'cca_cyclomatic_complexity_per_method': 'cca_cyclomatic_complexity_per_method',
        'maximum_cca_cyclomatic_complexity': 'maximum_cca_cyclomatic_complexity',
        'huge_cca_cyclomatic_complexity_total': 'huge_cca_cyclomatic_complexity_total',
        'cyclomatic_complexity_adequacy': 'cyclomatic_complexity_adequacy',
        'maximum_depth': 'maximum_depth',
        'huge_depth_total': 'huge_depth_total',
        'huge_depth_ratio': 'huge_depth_ratio',
        'method_lines': 'method_lines',
        'lines_per_method': 'lines_per_method',
        'huge_method_total': 'huge_method_total',
        'huge_method_ratio': 'huge_method_ratio',
        'files_total': 'files_total',
        'folders_total': 'folders_total',
        'lines_per_file': 'lines_per_file',
        'huge_headerfile_total': 'huge_headerfile_total',
        'huge_headerfile_ratio': 'huge_headerfile_ratio',
        'huge_non_headerfile_total': 'huge_non_headerfile_total',
        'huge_non_headerfile_ratio': 'huge_non_headerfile_ratio',
        'huge_folder_total': 'huge_folder_total',
        'huge_folder_ratio': 'huge_folder_ratio',
        'file_duplication_total': 'file_duplication_total',
        'file_duplication_ratio': 'file_duplication_ratio',
        'non_hfile_duplication_total': 'non_hfile_duplication_total',
        'non_hfile_duplication_ratio': 'non_hfile_duplication_ratio',
        'code_duplication_total': 'code_duplication_total',
        'code_duplication_ratio': 'code_duplication_ratio',
        'non_hfile_code_duplication_total': 'non_hfile_code_duplication_total',
        'non_hfile_code_duplication_ratio': 'non_hfile_code_duplication_ratio',
        'unsafe_functions_total': 'unsafe_functions_total',
        'unsafe_functions_kloc': 'unsafe_functions_kloc',
        'redundant_code_total': 'redundant_code_total',
        'redundant_code_kloc': 'redundant_code_kloc',
        'warning_suppression_total': 'warning_suppression_total',
        'warning_suppression_kloc': 'warning_suppression_kloc'
    }

    def __init__(self, code_size=None, raw_lines=None, methods_total=None, cyclomatic_complexity_total=None, cyclomatic_complexity_per_method=None, maximum_cyclomatic_complexity=None, huge_cyclomatic_complexity_total=None, huge_cyclomatic_complexity_ratio=None, cca_cyclomatic_complexity_total=None, cca_cyclomatic_complexity_per_method=None, maximum_cca_cyclomatic_complexity=None, huge_cca_cyclomatic_complexity_total=None, cyclomatic_complexity_adequacy=None, maximum_depth=None, huge_depth_total=None, huge_depth_ratio=None, method_lines=None, lines_per_method=None, huge_method_total=None, huge_method_ratio=None, files_total=None, folders_total=None, lines_per_file=None, huge_headerfile_total=None, huge_headerfile_ratio=None, huge_non_headerfile_total=None, huge_non_headerfile_ratio=None, huge_folder_total=None, huge_folder_ratio=None, file_duplication_total=None, file_duplication_ratio=None, non_hfile_duplication_total=None, non_hfile_duplication_ratio=None, code_duplication_total=None, code_duplication_ratio=None, non_hfile_code_duplication_total=None, non_hfile_code_duplication_ratio=None, unsafe_functions_total=None, unsafe_functions_kloc=None, redundant_code_total=None, redundant_code_kloc=None, warning_suppression_total=None, warning_suppression_kloc=None):
        """MetricInfo

        The model defined in huaweicloud sdk

        :param code_size: 代码规模
        :type code_size: str
        :param raw_lines: 原始代码行数
        :type raw_lines: str
        :param methods_total: 函数总数
        :type methods_total: str
        :param cyclomatic_complexity_total: 圈复杂度总数
        :type cyclomatic_complexity_total: str
        :param cyclomatic_complexity_per_method: 平均圈复杂度
        :type cyclomatic_complexity_per_method: str
        :param maximum_cyclomatic_complexity: 最大圈复杂度
        :type maximum_cyclomatic_complexity: str
        :param huge_cyclomatic_complexity_total: 超大圈复杂度数
        :type huge_cyclomatic_complexity_total: str
        :param huge_cyclomatic_complexity_ratio: 超大圈复杂度比例
        :type huge_cyclomatic_complexity_ratio: str
        :param cca_cyclomatic_complexity_total: cca圈复杂度总数
        :type cca_cyclomatic_complexity_total: str
        :param cca_cyclomatic_complexity_per_method: cca平均圈复杂度
        :type cca_cyclomatic_complexity_per_method: str
        :param maximum_cca_cyclomatic_complexity: cca最大圈复杂度
        :type maximum_cca_cyclomatic_complexity: str
        :param huge_cca_cyclomatic_complexity_total: 超大圈复杂度函数总数
        :type huge_cca_cyclomatic_complexity_total: str
        :param cyclomatic_complexity_adequacy: 圈复杂度满足度
        :type cyclomatic_complexity_adequacy: str
        :param maximum_depth: 最大深度
        :type maximum_depth: str
        :param huge_depth_total: 超大深度数
        :type huge_depth_total: str
        :param huge_depth_ratio: 超大深度占比
        :type huge_depth_ratio: str
        :param method_lines: 函数总行数
        :type method_lines: str
        :param lines_per_method: 函数平均代码行
        :type lines_per_method: str
        :param huge_method_total: 超大函数数
        :type huge_method_total: str
        :param huge_method_ratio: 超大函数占比
        :type huge_method_ratio: str
        :param files_total: 文件总数
        :type files_total: str
        :param folders_total: 目录总数
        :type folders_total: str
        :param lines_per_file: 文件平均代码行
        :type lines_per_file: str
        :param huge_headerfile_total: 超大头文件数
        :type huge_headerfile_total: str
        :param huge_headerfile_ratio: 超大头文件占比
        :type huge_headerfile_ratio: str
        :param huge_non_headerfile_total: 超大源文件数
        :type huge_non_headerfile_total: str
        :param huge_non_headerfile_ratio: 超大源文件占比
        :type huge_non_headerfile_ratio: str
        :param huge_folder_total: 超大目录数
        :type huge_folder_total: str
        :param huge_folder_ratio: 超大目录占比
        :type huge_folder_ratio: str
        :param file_duplication_total: 重复文件数
        :type file_duplication_total: str
        :param file_duplication_ratio: 文件重复率
        :type file_duplication_ratio: str
        :param non_hfile_duplication_total: 重复源文件数
        :type non_hfile_duplication_total: str
        :param non_hfile_duplication_ratio: 源文件重复率
        :type non_hfile_duplication_ratio: str
        :param code_duplication_total: 代码重复数
        :type code_duplication_total: str
        :param code_duplication_ratio: 代码重复率
        :type code_duplication_ratio: str
        :param non_hfile_code_duplication_total: 源文件代码重复数
        :type non_hfile_code_duplication_total: str
        :param non_hfile_code_duplication_ratio: 源文件代码重复率
        :type non_hfile_code_duplication_ratio: str
        :param unsafe_functions_total: 危险函数总数
        :type unsafe_functions_total: str
        :param unsafe_functions_kloc: 危险函数密度
        :type unsafe_functions_kloc: str
        :param redundant_code_total: 冗余代码数
        :type redundant_code_total: str
        :param redundant_code_kloc: 冗余代码块密度
        :type redundant_code_kloc: str
        :param warning_suppression_total: 抑制告警数
        :type warning_suppression_total: str
        :param warning_suppression_kloc: 抑制告警密度
        :type warning_suppression_kloc: str
        """
        
        

        self._code_size = None
        self._raw_lines = None
        self._methods_total = None
        self._cyclomatic_complexity_total = None
        self._cyclomatic_complexity_per_method = None
        self._maximum_cyclomatic_complexity = None
        self._huge_cyclomatic_complexity_total = None
        self._huge_cyclomatic_complexity_ratio = None
        self._cca_cyclomatic_complexity_total = None
        self._cca_cyclomatic_complexity_per_method = None
        self._maximum_cca_cyclomatic_complexity = None
        self._huge_cca_cyclomatic_complexity_total = None
        self._cyclomatic_complexity_adequacy = None
        self._maximum_depth = None
        self._huge_depth_total = None
        self._huge_depth_ratio = None
        self._method_lines = None
        self._lines_per_method = None
        self._huge_method_total = None
        self._huge_method_ratio = None
        self._files_total = None
        self._folders_total = None
        self._lines_per_file = None
        self._huge_headerfile_total = None
        self._huge_headerfile_ratio = None
        self._huge_non_headerfile_total = None
        self._huge_non_headerfile_ratio = None
        self._huge_folder_total = None
        self._huge_folder_ratio = None
        self._file_duplication_total = None
        self._file_duplication_ratio = None
        self._non_hfile_duplication_total = None
        self._non_hfile_duplication_ratio = None
        self._code_duplication_total = None
        self._code_duplication_ratio = None
        self._non_hfile_code_duplication_total = None
        self._non_hfile_code_duplication_ratio = None
        self._unsafe_functions_total = None
        self._unsafe_functions_kloc = None
        self._redundant_code_total = None
        self._redundant_code_kloc = None
        self._warning_suppression_total = None
        self._warning_suppression_kloc = None
        self.discriminator = None

        if code_size is not None:
            self.code_size = code_size
        if raw_lines is not None:
            self.raw_lines = raw_lines
        if methods_total is not None:
            self.methods_total = methods_total
        if cyclomatic_complexity_total is not None:
            self.cyclomatic_complexity_total = cyclomatic_complexity_total
        if cyclomatic_complexity_per_method is not None:
            self.cyclomatic_complexity_per_method = cyclomatic_complexity_per_method
        if maximum_cyclomatic_complexity is not None:
            self.maximum_cyclomatic_complexity = maximum_cyclomatic_complexity
        if huge_cyclomatic_complexity_total is not None:
            self.huge_cyclomatic_complexity_total = huge_cyclomatic_complexity_total
        if huge_cyclomatic_complexity_ratio is not None:
            self.huge_cyclomatic_complexity_ratio = huge_cyclomatic_complexity_ratio
        if cca_cyclomatic_complexity_total is not None:
            self.cca_cyclomatic_complexity_total = cca_cyclomatic_complexity_total
        if cca_cyclomatic_complexity_per_method is not None:
            self.cca_cyclomatic_complexity_per_method = cca_cyclomatic_complexity_per_method
        if maximum_cca_cyclomatic_complexity is not None:
            self.maximum_cca_cyclomatic_complexity = maximum_cca_cyclomatic_complexity
        if huge_cca_cyclomatic_complexity_total is not None:
            self.huge_cca_cyclomatic_complexity_total = huge_cca_cyclomatic_complexity_total
        if cyclomatic_complexity_adequacy is not None:
            self.cyclomatic_complexity_adequacy = cyclomatic_complexity_adequacy
        if maximum_depth is not None:
            self.maximum_depth = maximum_depth
        if huge_depth_total is not None:
            self.huge_depth_total = huge_depth_total
        if huge_depth_ratio is not None:
            self.huge_depth_ratio = huge_depth_ratio
        if method_lines is not None:
            self.method_lines = method_lines
        if lines_per_method is not None:
            self.lines_per_method = lines_per_method
        if huge_method_total is not None:
            self.huge_method_total = huge_method_total
        if huge_method_ratio is not None:
            self.huge_method_ratio = huge_method_ratio
        if files_total is not None:
            self.files_total = files_total
        if folders_total is not None:
            self.folders_total = folders_total
        if lines_per_file is not None:
            self.lines_per_file = lines_per_file
        if huge_headerfile_total is not None:
            self.huge_headerfile_total = huge_headerfile_total
        if huge_headerfile_ratio is not None:
            self.huge_headerfile_ratio = huge_headerfile_ratio
        if huge_non_headerfile_total is not None:
            self.huge_non_headerfile_total = huge_non_headerfile_total
        if huge_non_headerfile_ratio is not None:
            self.huge_non_headerfile_ratio = huge_non_headerfile_ratio
        if huge_folder_total is not None:
            self.huge_folder_total = huge_folder_total
        if huge_folder_ratio is not None:
            self.huge_folder_ratio = huge_folder_ratio
        if file_duplication_total is not None:
            self.file_duplication_total = file_duplication_total
        if file_duplication_ratio is not None:
            self.file_duplication_ratio = file_duplication_ratio
        if non_hfile_duplication_total is not None:
            self.non_hfile_duplication_total = non_hfile_duplication_total
        if non_hfile_duplication_ratio is not None:
            self.non_hfile_duplication_ratio = non_hfile_duplication_ratio
        if code_duplication_total is not None:
            self.code_duplication_total = code_duplication_total
        if code_duplication_ratio is not None:
            self.code_duplication_ratio = code_duplication_ratio
        if non_hfile_code_duplication_total is not None:
            self.non_hfile_code_duplication_total = non_hfile_code_duplication_total
        if non_hfile_code_duplication_ratio is not None:
            self.non_hfile_code_duplication_ratio = non_hfile_code_duplication_ratio
        if unsafe_functions_total is not None:
            self.unsafe_functions_total = unsafe_functions_total
        if unsafe_functions_kloc is not None:
            self.unsafe_functions_kloc = unsafe_functions_kloc
        if redundant_code_total is not None:
            self.redundant_code_total = redundant_code_total
        if redundant_code_kloc is not None:
            self.redundant_code_kloc = redundant_code_kloc
        if warning_suppression_total is not None:
            self.warning_suppression_total = warning_suppression_total
        if warning_suppression_kloc is not None:
            self.warning_suppression_kloc = warning_suppression_kloc

    @property
    def code_size(self):
        """Gets the code_size of this MetricInfo.

        代码规模

        :return: The code_size of this MetricInfo.
        :rtype: str
        """
        return self._code_size

    @code_size.setter
    def code_size(self, code_size):
        """Sets the code_size of this MetricInfo.

        代码规模

        :param code_size: The code_size of this MetricInfo.
        :type code_size: str
        """
        self._code_size = code_size

    @property
    def raw_lines(self):
        """Gets the raw_lines of this MetricInfo.

        原始代码行数

        :return: The raw_lines of this MetricInfo.
        :rtype: str
        """
        return self._raw_lines

    @raw_lines.setter
    def raw_lines(self, raw_lines):
        """Sets the raw_lines of this MetricInfo.

        原始代码行数

        :param raw_lines: The raw_lines of this MetricInfo.
        :type raw_lines: str
        """
        self._raw_lines = raw_lines

    @property
    def methods_total(self):
        """Gets the methods_total of this MetricInfo.

        函数总数

        :return: The methods_total of this MetricInfo.
        :rtype: str
        """
        return self._methods_total

    @methods_total.setter
    def methods_total(self, methods_total):
        """Sets the methods_total of this MetricInfo.

        函数总数

        :param methods_total: The methods_total of this MetricInfo.
        :type methods_total: str
        """
        self._methods_total = methods_total

    @property
    def cyclomatic_complexity_total(self):
        """Gets the cyclomatic_complexity_total of this MetricInfo.

        圈复杂度总数

        :return: The cyclomatic_complexity_total of this MetricInfo.
        :rtype: str
        """
        return self._cyclomatic_complexity_total

    @cyclomatic_complexity_total.setter
    def cyclomatic_complexity_total(self, cyclomatic_complexity_total):
        """Sets the cyclomatic_complexity_total of this MetricInfo.

        圈复杂度总数

        :param cyclomatic_complexity_total: The cyclomatic_complexity_total of this MetricInfo.
        :type cyclomatic_complexity_total: str
        """
        self._cyclomatic_complexity_total = cyclomatic_complexity_total

    @property
    def cyclomatic_complexity_per_method(self):
        """Gets the cyclomatic_complexity_per_method of this MetricInfo.

        平均圈复杂度

        :return: The cyclomatic_complexity_per_method of this MetricInfo.
        :rtype: str
        """
        return self._cyclomatic_complexity_per_method

    @cyclomatic_complexity_per_method.setter
    def cyclomatic_complexity_per_method(self, cyclomatic_complexity_per_method):
        """Sets the cyclomatic_complexity_per_method of this MetricInfo.

        平均圈复杂度

        :param cyclomatic_complexity_per_method: The cyclomatic_complexity_per_method of this MetricInfo.
        :type cyclomatic_complexity_per_method: str
        """
        self._cyclomatic_complexity_per_method = cyclomatic_complexity_per_method

    @property
    def maximum_cyclomatic_complexity(self):
        """Gets the maximum_cyclomatic_complexity of this MetricInfo.

        最大圈复杂度

        :return: The maximum_cyclomatic_complexity of this MetricInfo.
        :rtype: str
        """
        return self._maximum_cyclomatic_complexity

    @maximum_cyclomatic_complexity.setter
    def maximum_cyclomatic_complexity(self, maximum_cyclomatic_complexity):
        """Sets the maximum_cyclomatic_complexity of this MetricInfo.

        最大圈复杂度

        :param maximum_cyclomatic_complexity: The maximum_cyclomatic_complexity of this MetricInfo.
        :type maximum_cyclomatic_complexity: str
        """
        self._maximum_cyclomatic_complexity = maximum_cyclomatic_complexity

    @property
    def huge_cyclomatic_complexity_total(self):
        """Gets the huge_cyclomatic_complexity_total of this MetricInfo.

        超大圈复杂度数

        :return: The huge_cyclomatic_complexity_total of this MetricInfo.
        :rtype: str
        """
        return self._huge_cyclomatic_complexity_total

    @huge_cyclomatic_complexity_total.setter
    def huge_cyclomatic_complexity_total(self, huge_cyclomatic_complexity_total):
        """Sets the huge_cyclomatic_complexity_total of this MetricInfo.

        超大圈复杂度数

        :param huge_cyclomatic_complexity_total: The huge_cyclomatic_complexity_total of this MetricInfo.
        :type huge_cyclomatic_complexity_total: str
        """
        self._huge_cyclomatic_complexity_total = huge_cyclomatic_complexity_total

    @property
    def huge_cyclomatic_complexity_ratio(self):
        """Gets the huge_cyclomatic_complexity_ratio of this MetricInfo.

        超大圈复杂度比例

        :return: The huge_cyclomatic_complexity_ratio of this MetricInfo.
        :rtype: str
        """
        return self._huge_cyclomatic_complexity_ratio

    @huge_cyclomatic_complexity_ratio.setter
    def huge_cyclomatic_complexity_ratio(self, huge_cyclomatic_complexity_ratio):
        """Sets the huge_cyclomatic_complexity_ratio of this MetricInfo.

        超大圈复杂度比例

        :param huge_cyclomatic_complexity_ratio: The huge_cyclomatic_complexity_ratio of this MetricInfo.
        :type huge_cyclomatic_complexity_ratio: str
        """
        self._huge_cyclomatic_complexity_ratio = huge_cyclomatic_complexity_ratio

    @property
    def cca_cyclomatic_complexity_total(self):
        """Gets the cca_cyclomatic_complexity_total of this MetricInfo.

        cca圈复杂度总数

        :return: The cca_cyclomatic_complexity_total of this MetricInfo.
        :rtype: str
        """
        return self._cca_cyclomatic_complexity_total

    @cca_cyclomatic_complexity_total.setter
    def cca_cyclomatic_complexity_total(self, cca_cyclomatic_complexity_total):
        """Sets the cca_cyclomatic_complexity_total of this MetricInfo.

        cca圈复杂度总数

        :param cca_cyclomatic_complexity_total: The cca_cyclomatic_complexity_total of this MetricInfo.
        :type cca_cyclomatic_complexity_total: str
        """
        self._cca_cyclomatic_complexity_total = cca_cyclomatic_complexity_total

    @property
    def cca_cyclomatic_complexity_per_method(self):
        """Gets the cca_cyclomatic_complexity_per_method of this MetricInfo.

        cca平均圈复杂度

        :return: The cca_cyclomatic_complexity_per_method of this MetricInfo.
        :rtype: str
        """
        return self._cca_cyclomatic_complexity_per_method

    @cca_cyclomatic_complexity_per_method.setter
    def cca_cyclomatic_complexity_per_method(self, cca_cyclomatic_complexity_per_method):
        """Sets the cca_cyclomatic_complexity_per_method of this MetricInfo.

        cca平均圈复杂度

        :param cca_cyclomatic_complexity_per_method: The cca_cyclomatic_complexity_per_method of this MetricInfo.
        :type cca_cyclomatic_complexity_per_method: str
        """
        self._cca_cyclomatic_complexity_per_method = cca_cyclomatic_complexity_per_method

    @property
    def maximum_cca_cyclomatic_complexity(self):
        """Gets the maximum_cca_cyclomatic_complexity of this MetricInfo.

        cca最大圈复杂度

        :return: The maximum_cca_cyclomatic_complexity of this MetricInfo.
        :rtype: str
        """
        return self._maximum_cca_cyclomatic_complexity

    @maximum_cca_cyclomatic_complexity.setter
    def maximum_cca_cyclomatic_complexity(self, maximum_cca_cyclomatic_complexity):
        """Sets the maximum_cca_cyclomatic_complexity of this MetricInfo.

        cca最大圈复杂度

        :param maximum_cca_cyclomatic_complexity: The maximum_cca_cyclomatic_complexity of this MetricInfo.
        :type maximum_cca_cyclomatic_complexity: str
        """
        self._maximum_cca_cyclomatic_complexity = maximum_cca_cyclomatic_complexity

    @property
    def huge_cca_cyclomatic_complexity_total(self):
        """Gets the huge_cca_cyclomatic_complexity_total of this MetricInfo.

        超大圈复杂度函数总数

        :return: The huge_cca_cyclomatic_complexity_total of this MetricInfo.
        :rtype: str
        """
        return self._huge_cca_cyclomatic_complexity_total

    @huge_cca_cyclomatic_complexity_total.setter
    def huge_cca_cyclomatic_complexity_total(self, huge_cca_cyclomatic_complexity_total):
        """Sets the huge_cca_cyclomatic_complexity_total of this MetricInfo.

        超大圈复杂度函数总数

        :param huge_cca_cyclomatic_complexity_total: The huge_cca_cyclomatic_complexity_total of this MetricInfo.
        :type huge_cca_cyclomatic_complexity_total: str
        """
        self._huge_cca_cyclomatic_complexity_total = huge_cca_cyclomatic_complexity_total

    @property
    def cyclomatic_complexity_adequacy(self):
        """Gets the cyclomatic_complexity_adequacy of this MetricInfo.

        圈复杂度满足度

        :return: The cyclomatic_complexity_adequacy of this MetricInfo.
        :rtype: str
        """
        return self._cyclomatic_complexity_adequacy

    @cyclomatic_complexity_adequacy.setter
    def cyclomatic_complexity_adequacy(self, cyclomatic_complexity_adequacy):
        """Sets the cyclomatic_complexity_adequacy of this MetricInfo.

        圈复杂度满足度

        :param cyclomatic_complexity_adequacy: The cyclomatic_complexity_adequacy of this MetricInfo.
        :type cyclomatic_complexity_adequacy: str
        """
        self._cyclomatic_complexity_adequacy = cyclomatic_complexity_adequacy

    @property
    def maximum_depth(self):
        """Gets the maximum_depth of this MetricInfo.

        最大深度

        :return: The maximum_depth of this MetricInfo.
        :rtype: str
        """
        return self._maximum_depth

    @maximum_depth.setter
    def maximum_depth(self, maximum_depth):
        """Sets the maximum_depth of this MetricInfo.

        最大深度

        :param maximum_depth: The maximum_depth of this MetricInfo.
        :type maximum_depth: str
        """
        self._maximum_depth = maximum_depth

    @property
    def huge_depth_total(self):
        """Gets the huge_depth_total of this MetricInfo.

        超大深度数

        :return: The huge_depth_total of this MetricInfo.
        :rtype: str
        """
        return self._huge_depth_total

    @huge_depth_total.setter
    def huge_depth_total(self, huge_depth_total):
        """Sets the huge_depth_total of this MetricInfo.

        超大深度数

        :param huge_depth_total: The huge_depth_total of this MetricInfo.
        :type huge_depth_total: str
        """
        self._huge_depth_total = huge_depth_total

    @property
    def huge_depth_ratio(self):
        """Gets the huge_depth_ratio of this MetricInfo.

        超大深度占比

        :return: The huge_depth_ratio of this MetricInfo.
        :rtype: str
        """
        return self._huge_depth_ratio

    @huge_depth_ratio.setter
    def huge_depth_ratio(self, huge_depth_ratio):
        """Sets the huge_depth_ratio of this MetricInfo.

        超大深度占比

        :param huge_depth_ratio: The huge_depth_ratio of this MetricInfo.
        :type huge_depth_ratio: str
        """
        self._huge_depth_ratio = huge_depth_ratio

    @property
    def method_lines(self):
        """Gets the method_lines of this MetricInfo.

        函数总行数

        :return: The method_lines of this MetricInfo.
        :rtype: str
        """
        return self._method_lines

    @method_lines.setter
    def method_lines(self, method_lines):
        """Sets the method_lines of this MetricInfo.

        函数总行数

        :param method_lines: The method_lines of this MetricInfo.
        :type method_lines: str
        """
        self._method_lines = method_lines

    @property
    def lines_per_method(self):
        """Gets the lines_per_method of this MetricInfo.

        函数平均代码行

        :return: The lines_per_method of this MetricInfo.
        :rtype: str
        """
        return self._lines_per_method

    @lines_per_method.setter
    def lines_per_method(self, lines_per_method):
        """Sets the lines_per_method of this MetricInfo.

        函数平均代码行

        :param lines_per_method: The lines_per_method of this MetricInfo.
        :type lines_per_method: str
        """
        self._lines_per_method = lines_per_method

    @property
    def huge_method_total(self):
        """Gets the huge_method_total of this MetricInfo.

        超大函数数

        :return: The huge_method_total of this MetricInfo.
        :rtype: str
        """
        return self._huge_method_total

    @huge_method_total.setter
    def huge_method_total(self, huge_method_total):
        """Sets the huge_method_total of this MetricInfo.

        超大函数数

        :param huge_method_total: The huge_method_total of this MetricInfo.
        :type huge_method_total: str
        """
        self._huge_method_total = huge_method_total

    @property
    def huge_method_ratio(self):
        """Gets the huge_method_ratio of this MetricInfo.

        超大函数占比

        :return: The huge_method_ratio of this MetricInfo.
        :rtype: str
        """
        return self._huge_method_ratio

    @huge_method_ratio.setter
    def huge_method_ratio(self, huge_method_ratio):
        """Sets the huge_method_ratio of this MetricInfo.

        超大函数占比

        :param huge_method_ratio: The huge_method_ratio of this MetricInfo.
        :type huge_method_ratio: str
        """
        self._huge_method_ratio = huge_method_ratio

    @property
    def files_total(self):
        """Gets the files_total of this MetricInfo.

        文件总数

        :return: The files_total of this MetricInfo.
        :rtype: str
        """
        return self._files_total

    @files_total.setter
    def files_total(self, files_total):
        """Sets the files_total of this MetricInfo.

        文件总数

        :param files_total: The files_total of this MetricInfo.
        :type files_total: str
        """
        self._files_total = files_total

    @property
    def folders_total(self):
        """Gets the folders_total of this MetricInfo.

        目录总数

        :return: The folders_total of this MetricInfo.
        :rtype: str
        """
        return self._folders_total

    @folders_total.setter
    def folders_total(self, folders_total):
        """Sets the folders_total of this MetricInfo.

        目录总数

        :param folders_total: The folders_total of this MetricInfo.
        :type folders_total: str
        """
        self._folders_total = folders_total

    @property
    def lines_per_file(self):
        """Gets the lines_per_file of this MetricInfo.

        文件平均代码行

        :return: The lines_per_file of this MetricInfo.
        :rtype: str
        """
        return self._lines_per_file

    @lines_per_file.setter
    def lines_per_file(self, lines_per_file):
        """Sets the lines_per_file of this MetricInfo.

        文件平均代码行

        :param lines_per_file: The lines_per_file of this MetricInfo.
        :type lines_per_file: str
        """
        self._lines_per_file = lines_per_file

    @property
    def huge_headerfile_total(self):
        """Gets the huge_headerfile_total of this MetricInfo.

        超大头文件数

        :return: The huge_headerfile_total of this MetricInfo.
        :rtype: str
        """
        return self._huge_headerfile_total

    @huge_headerfile_total.setter
    def huge_headerfile_total(self, huge_headerfile_total):
        """Sets the huge_headerfile_total of this MetricInfo.

        超大头文件数

        :param huge_headerfile_total: The huge_headerfile_total of this MetricInfo.
        :type huge_headerfile_total: str
        """
        self._huge_headerfile_total = huge_headerfile_total

    @property
    def huge_headerfile_ratio(self):
        """Gets the huge_headerfile_ratio of this MetricInfo.

        超大头文件占比

        :return: The huge_headerfile_ratio of this MetricInfo.
        :rtype: str
        """
        return self._huge_headerfile_ratio

    @huge_headerfile_ratio.setter
    def huge_headerfile_ratio(self, huge_headerfile_ratio):
        """Sets the huge_headerfile_ratio of this MetricInfo.

        超大头文件占比

        :param huge_headerfile_ratio: The huge_headerfile_ratio of this MetricInfo.
        :type huge_headerfile_ratio: str
        """
        self._huge_headerfile_ratio = huge_headerfile_ratio

    @property
    def huge_non_headerfile_total(self):
        """Gets the huge_non_headerfile_total of this MetricInfo.

        超大源文件数

        :return: The huge_non_headerfile_total of this MetricInfo.
        :rtype: str
        """
        return self._huge_non_headerfile_total

    @huge_non_headerfile_total.setter
    def huge_non_headerfile_total(self, huge_non_headerfile_total):
        """Sets the huge_non_headerfile_total of this MetricInfo.

        超大源文件数

        :param huge_non_headerfile_total: The huge_non_headerfile_total of this MetricInfo.
        :type huge_non_headerfile_total: str
        """
        self._huge_non_headerfile_total = huge_non_headerfile_total

    @property
    def huge_non_headerfile_ratio(self):
        """Gets the huge_non_headerfile_ratio of this MetricInfo.

        超大源文件占比

        :return: The huge_non_headerfile_ratio of this MetricInfo.
        :rtype: str
        """
        return self._huge_non_headerfile_ratio

    @huge_non_headerfile_ratio.setter
    def huge_non_headerfile_ratio(self, huge_non_headerfile_ratio):
        """Sets the huge_non_headerfile_ratio of this MetricInfo.

        超大源文件占比

        :param huge_non_headerfile_ratio: The huge_non_headerfile_ratio of this MetricInfo.
        :type huge_non_headerfile_ratio: str
        """
        self._huge_non_headerfile_ratio = huge_non_headerfile_ratio

    @property
    def huge_folder_total(self):
        """Gets the huge_folder_total of this MetricInfo.

        超大目录数

        :return: The huge_folder_total of this MetricInfo.
        :rtype: str
        """
        return self._huge_folder_total

    @huge_folder_total.setter
    def huge_folder_total(self, huge_folder_total):
        """Sets the huge_folder_total of this MetricInfo.

        超大目录数

        :param huge_folder_total: The huge_folder_total of this MetricInfo.
        :type huge_folder_total: str
        """
        self._huge_folder_total = huge_folder_total

    @property
    def huge_folder_ratio(self):
        """Gets the huge_folder_ratio of this MetricInfo.

        超大目录占比

        :return: The huge_folder_ratio of this MetricInfo.
        :rtype: str
        """
        return self._huge_folder_ratio

    @huge_folder_ratio.setter
    def huge_folder_ratio(self, huge_folder_ratio):
        """Sets the huge_folder_ratio of this MetricInfo.

        超大目录占比

        :param huge_folder_ratio: The huge_folder_ratio of this MetricInfo.
        :type huge_folder_ratio: str
        """
        self._huge_folder_ratio = huge_folder_ratio

    @property
    def file_duplication_total(self):
        """Gets the file_duplication_total of this MetricInfo.

        重复文件数

        :return: The file_duplication_total of this MetricInfo.
        :rtype: str
        """
        return self._file_duplication_total

    @file_duplication_total.setter
    def file_duplication_total(self, file_duplication_total):
        """Sets the file_duplication_total of this MetricInfo.

        重复文件数

        :param file_duplication_total: The file_duplication_total of this MetricInfo.
        :type file_duplication_total: str
        """
        self._file_duplication_total = file_duplication_total

    @property
    def file_duplication_ratio(self):
        """Gets the file_duplication_ratio of this MetricInfo.

        文件重复率

        :return: The file_duplication_ratio of this MetricInfo.
        :rtype: str
        """
        return self._file_duplication_ratio

    @file_duplication_ratio.setter
    def file_duplication_ratio(self, file_duplication_ratio):
        """Sets the file_duplication_ratio of this MetricInfo.

        文件重复率

        :param file_duplication_ratio: The file_duplication_ratio of this MetricInfo.
        :type file_duplication_ratio: str
        """
        self._file_duplication_ratio = file_duplication_ratio

    @property
    def non_hfile_duplication_total(self):
        """Gets the non_hfile_duplication_total of this MetricInfo.

        重复源文件数

        :return: The non_hfile_duplication_total of this MetricInfo.
        :rtype: str
        """
        return self._non_hfile_duplication_total

    @non_hfile_duplication_total.setter
    def non_hfile_duplication_total(self, non_hfile_duplication_total):
        """Sets the non_hfile_duplication_total of this MetricInfo.

        重复源文件数

        :param non_hfile_duplication_total: The non_hfile_duplication_total of this MetricInfo.
        :type non_hfile_duplication_total: str
        """
        self._non_hfile_duplication_total = non_hfile_duplication_total

    @property
    def non_hfile_duplication_ratio(self):
        """Gets the non_hfile_duplication_ratio of this MetricInfo.

        源文件重复率

        :return: The non_hfile_duplication_ratio of this MetricInfo.
        :rtype: str
        """
        return self._non_hfile_duplication_ratio

    @non_hfile_duplication_ratio.setter
    def non_hfile_duplication_ratio(self, non_hfile_duplication_ratio):
        """Sets the non_hfile_duplication_ratio of this MetricInfo.

        源文件重复率

        :param non_hfile_duplication_ratio: The non_hfile_duplication_ratio of this MetricInfo.
        :type non_hfile_duplication_ratio: str
        """
        self._non_hfile_duplication_ratio = non_hfile_duplication_ratio

    @property
    def code_duplication_total(self):
        """Gets the code_duplication_total of this MetricInfo.

        代码重复数

        :return: The code_duplication_total of this MetricInfo.
        :rtype: str
        """
        return self._code_duplication_total

    @code_duplication_total.setter
    def code_duplication_total(self, code_duplication_total):
        """Sets the code_duplication_total of this MetricInfo.

        代码重复数

        :param code_duplication_total: The code_duplication_total of this MetricInfo.
        :type code_duplication_total: str
        """
        self._code_duplication_total = code_duplication_total

    @property
    def code_duplication_ratio(self):
        """Gets the code_duplication_ratio of this MetricInfo.

        代码重复率

        :return: The code_duplication_ratio of this MetricInfo.
        :rtype: str
        """
        return self._code_duplication_ratio

    @code_duplication_ratio.setter
    def code_duplication_ratio(self, code_duplication_ratio):
        """Sets the code_duplication_ratio of this MetricInfo.

        代码重复率

        :param code_duplication_ratio: The code_duplication_ratio of this MetricInfo.
        :type code_duplication_ratio: str
        """
        self._code_duplication_ratio = code_duplication_ratio

    @property
    def non_hfile_code_duplication_total(self):
        """Gets the non_hfile_code_duplication_total of this MetricInfo.

        源文件代码重复数

        :return: The non_hfile_code_duplication_total of this MetricInfo.
        :rtype: str
        """
        return self._non_hfile_code_duplication_total

    @non_hfile_code_duplication_total.setter
    def non_hfile_code_duplication_total(self, non_hfile_code_duplication_total):
        """Sets the non_hfile_code_duplication_total of this MetricInfo.

        源文件代码重复数

        :param non_hfile_code_duplication_total: The non_hfile_code_duplication_total of this MetricInfo.
        :type non_hfile_code_duplication_total: str
        """
        self._non_hfile_code_duplication_total = non_hfile_code_duplication_total

    @property
    def non_hfile_code_duplication_ratio(self):
        """Gets the non_hfile_code_duplication_ratio of this MetricInfo.

        源文件代码重复率

        :return: The non_hfile_code_duplication_ratio of this MetricInfo.
        :rtype: str
        """
        return self._non_hfile_code_duplication_ratio

    @non_hfile_code_duplication_ratio.setter
    def non_hfile_code_duplication_ratio(self, non_hfile_code_duplication_ratio):
        """Sets the non_hfile_code_duplication_ratio of this MetricInfo.

        源文件代码重复率

        :param non_hfile_code_duplication_ratio: The non_hfile_code_duplication_ratio of this MetricInfo.
        :type non_hfile_code_duplication_ratio: str
        """
        self._non_hfile_code_duplication_ratio = non_hfile_code_duplication_ratio

    @property
    def unsafe_functions_total(self):
        """Gets the unsafe_functions_total of this MetricInfo.

        危险函数总数

        :return: The unsafe_functions_total of this MetricInfo.
        :rtype: str
        """
        return self._unsafe_functions_total

    @unsafe_functions_total.setter
    def unsafe_functions_total(self, unsafe_functions_total):
        """Sets the unsafe_functions_total of this MetricInfo.

        危险函数总数

        :param unsafe_functions_total: The unsafe_functions_total of this MetricInfo.
        :type unsafe_functions_total: str
        """
        self._unsafe_functions_total = unsafe_functions_total

    @property
    def unsafe_functions_kloc(self):
        """Gets the unsafe_functions_kloc of this MetricInfo.

        危险函数密度

        :return: The unsafe_functions_kloc of this MetricInfo.
        :rtype: str
        """
        return self._unsafe_functions_kloc

    @unsafe_functions_kloc.setter
    def unsafe_functions_kloc(self, unsafe_functions_kloc):
        """Sets the unsafe_functions_kloc of this MetricInfo.

        危险函数密度

        :param unsafe_functions_kloc: The unsafe_functions_kloc of this MetricInfo.
        :type unsafe_functions_kloc: str
        """
        self._unsafe_functions_kloc = unsafe_functions_kloc

    @property
    def redundant_code_total(self):
        """Gets the redundant_code_total of this MetricInfo.

        冗余代码数

        :return: The redundant_code_total of this MetricInfo.
        :rtype: str
        """
        return self._redundant_code_total

    @redundant_code_total.setter
    def redundant_code_total(self, redundant_code_total):
        """Sets the redundant_code_total of this MetricInfo.

        冗余代码数

        :param redundant_code_total: The redundant_code_total of this MetricInfo.
        :type redundant_code_total: str
        """
        self._redundant_code_total = redundant_code_total

    @property
    def redundant_code_kloc(self):
        """Gets the redundant_code_kloc of this MetricInfo.

        冗余代码块密度

        :return: The redundant_code_kloc of this MetricInfo.
        :rtype: str
        """
        return self._redundant_code_kloc

    @redundant_code_kloc.setter
    def redundant_code_kloc(self, redundant_code_kloc):
        """Sets the redundant_code_kloc of this MetricInfo.

        冗余代码块密度

        :param redundant_code_kloc: The redundant_code_kloc of this MetricInfo.
        :type redundant_code_kloc: str
        """
        self._redundant_code_kloc = redundant_code_kloc

    @property
    def warning_suppression_total(self):
        """Gets the warning_suppression_total of this MetricInfo.

        抑制告警数

        :return: The warning_suppression_total of this MetricInfo.
        :rtype: str
        """
        return self._warning_suppression_total

    @warning_suppression_total.setter
    def warning_suppression_total(self, warning_suppression_total):
        """Sets the warning_suppression_total of this MetricInfo.

        抑制告警数

        :param warning_suppression_total: The warning_suppression_total of this MetricInfo.
        :type warning_suppression_total: str
        """
        self._warning_suppression_total = warning_suppression_total

    @property
    def warning_suppression_kloc(self):
        """Gets the warning_suppression_kloc of this MetricInfo.

        抑制告警密度

        :return: The warning_suppression_kloc of this MetricInfo.
        :rtype: str
        """
        return self._warning_suppression_kloc

    @warning_suppression_kloc.setter
    def warning_suppression_kloc(self, warning_suppression_kloc):
        """Sets the warning_suppression_kloc of this MetricInfo.

        抑制告警密度

        :param warning_suppression_kloc: The warning_suppression_kloc of this MetricInfo.
        :type warning_suppression_kloc: str
        """
        self._warning_suppression_kloc = warning_suppression_kloc

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetricInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
