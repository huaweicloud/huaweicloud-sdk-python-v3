# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OprReportInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'int',
        'workpiece_type': 'str',
        'analysis_dim_row': 'str',
        'compare_dim_column': 'str',
        'filter': 'ReportFilter'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'workpiece_type': 'workpiece_type',
        'analysis_dim_row': 'analysis_dim_row',
        'compare_dim_column': 'compare_dim_column',
        'filter': 'filter'
    }

    def __init__(self, name=None, type=None, workpiece_type=None, analysis_dim_row=None, compare_dim_column=None, filter=None):
        r"""OprReportInfo

        The model defined in huaweicloud sdk

        :param name: 报表名称
        :type name: str
        :param type: 报表类型 1：首页用例库， 2：质量报告
        :type type: int
        :param workpiece_type: 工件类型(用例：case,测试套：suite)
        :type workpiece_type: str
        :param analysis_dim_row: 分析维度
        :type analysis_dim_row: str
        :param compare_dim_column: 对比维度
        :type compare_dim_column: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkcloudtest.v1.ReportFilter`
        """
        
        

        self._name = None
        self._type = None
        self._workpiece_type = None
        self._analysis_dim_row = None
        self._compare_dim_column = None
        self._filter = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if workpiece_type is not None:
            self.workpiece_type = workpiece_type
        if analysis_dim_row is not None:
            self.analysis_dim_row = analysis_dim_row
        if compare_dim_column is not None:
            self.compare_dim_column = compare_dim_column
        if filter is not None:
            self.filter = filter

    @property
    def name(self):
        r"""Gets the name of this OprReportInfo.

        报表名称

        :return: The name of this OprReportInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OprReportInfo.

        报表名称

        :param name: The name of this OprReportInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this OprReportInfo.

        报表类型 1：首页用例库， 2：质量报告

        :return: The type of this OprReportInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OprReportInfo.

        报表类型 1：首页用例库， 2：质量报告

        :param type: The type of this OprReportInfo.
        :type type: int
        """
        self._type = type

    @property
    def workpiece_type(self):
        r"""Gets the workpiece_type of this OprReportInfo.

        工件类型(用例：case,测试套：suite)

        :return: The workpiece_type of this OprReportInfo.
        :rtype: str
        """
        return self._workpiece_type

    @workpiece_type.setter
    def workpiece_type(self, workpiece_type):
        r"""Sets the workpiece_type of this OprReportInfo.

        工件类型(用例：case,测试套：suite)

        :param workpiece_type: The workpiece_type of this OprReportInfo.
        :type workpiece_type: str
        """
        self._workpiece_type = workpiece_type

    @property
    def analysis_dim_row(self):
        r"""Gets the analysis_dim_row of this OprReportInfo.

        分析维度

        :return: The analysis_dim_row of this OprReportInfo.
        :rtype: str
        """
        return self._analysis_dim_row

    @analysis_dim_row.setter
    def analysis_dim_row(self, analysis_dim_row):
        r"""Sets the analysis_dim_row of this OprReportInfo.

        分析维度

        :param analysis_dim_row: The analysis_dim_row of this OprReportInfo.
        :type analysis_dim_row: str
        """
        self._analysis_dim_row = analysis_dim_row

    @property
    def compare_dim_column(self):
        r"""Gets the compare_dim_column of this OprReportInfo.

        对比维度

        :return: The compare_dim_column of this OprReportInfo.
        :rtype: str
        """
        return self._compare_dim_column

    @compare_dim_column.setter
    def compare_dim_column(self, compare_dim_column):
        r"""Sets the compare_dim_column of this OprReportInfo.

        对比维度

        :param compare_dim_column: The compare_dim_column of this OprReportInfo.
        :type compare_dim_column: str
        """
        self._compare_dim_column = compare_dim_column

    @property
    def filter(self):
        r"""Gets the filter of this OprReportInfo.

        :return: The filter of this OprReportInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ReportFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this OprReportInfo.

        :param filter: The filter of this OprReportInfo.
        :type filter: :class:`huaweicloudsdkcloudtest.v1.ReportFilter`
        """
        self._filter = filter

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
        if not isinstance(other, OprReportInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
