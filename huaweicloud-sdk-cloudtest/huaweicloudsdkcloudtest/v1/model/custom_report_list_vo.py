# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomReportListVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'filter': 'ReportFilter',
        'workpiece_type': 'str',
        'analysis_dimension': 'str',
        'compare_dimension': 'str',
        'chart_data': 'list[ReportChartDataVo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'filter': 'filter',
        'workpiece_type': 'workpiece_type',
        'analysis_dimension': 'analysis_dimension',
        'compare_dimension': 'compare_dimension',
        'chart_data': 'chart_data'
    }

    def __init__(self, id=None, name=None, filter=None, workpiece_type=None, analysis_dimension=None, compare_dimension=None, chart_data=None):
        r"""CustomReportListVo

        The model defined in huaweicloud sdk

        :param id: 报表id
        :type id: str
        :param name: 报表名称
        :type name: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkcloudtest.v1.ReportFilter`
        :param workpiece_type: 工件类型(用例：case,测试套：task)
        :type workpiece_type: str
        :param analysis_dimension: 分析维度
        :type analysis_dimension: str
        :param compare_dimension: 对比维度
        :type compare_dimension: str
        :param chart_data: 报表数据
        :type chart_data: list[:class:`huaweicloudsdkcloudtest.v1.ReportChartDataVo`]
        """
        
        

        self._id = None
        self._name = None
        self._filter = None
        self._workpiece_type = None
        self._analysis_dimension = None
        self._compare_dimension = None
        self._chart_data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if filter is not None:
            self.filter = filter
        if workpiece_type is not None:
            self.workpiece_type = workpiece_type
        if analysis_dimension is not None:
            self.analysis_dimension = analysis_dimension
        if compare_dimension is not None:
            self.compare_dimension = compare_dimension
        if chart_data is not None:
            self.chart_data = chart_data

    @property
    def id(self):
        r"""Gets the id of this CustomReportListVo.

        报表id

        :return: The id of this CustomReportListVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomReportListVo.

        报表id

        :param id: The id of this CustomReportListVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CustomReportListVo.

        报表名称

        :return: The name of this CustomReportListVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomReportListVo.

        报表名称

        :param name: The name of this CustomReportListVo.
        :type name: str
        """
        self._name = name

    @property
    def filter(self):
        r"""Gets the filter of this CustomReportListVo.

        :return: The filter of this CustomReportListVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ReportFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this CustomReportListVo.

        :param filter: The filter of this CustomReportListVo.
        :type filter: :class:`huaweicloudsdkcloudtest.v1.ReportFilter`
        """
        self._filter = filter

    @property
    def workpiece_type(self):
        r"""Gets the workpiece_type of this CustomReportListVo.

        工件类型(用例：case,测试套：task)

        :return: The workpiece_type of this CustomReportListVo.
        :rtype: str
        """
        return self._workpiece_type

    @workpiece_type.setter
    def workpiece_type(self, workpiece_type):
        r"""Sets the workpiece_type of this CustomReportListVo.

        工件类型(用例：case,测试套：task)

        :param workpiece_type: The workpiece_type of this CustomReportListVo.
        :type workpiece_type: str
        """
        self._workpiece_type = workpiece_type

    @property
    def analysis_dimension(self):
        r"""Gets the analysis_dimension of this CustomReportListVo.

        分析维度

        :return: The analysis_dimension of this CustomReportListVo.
        :rtype: str
        """
        return self._analysis_dimension

    @analysis_dimension.setter
    def analysis_dimension(self, analysis_dimension):
        r"""Sets the analysis_dimension of this CustomReportListVo.

        分析维度

        :param analysis_dimension: The analysis_dimension of this CustomReportListVo.
        :type analysis_dimension: str
        """
        self._analysis_dimension = analysis_dimension

    @property
    def compare_dimension(self):
        r"""Gets the compare_dimension of this CustomReportListVo.

        对比维度

        :return: The compare_dimension of this CustomReportListVo.
        :rtype: str
        """
        return self._compare_dimension

    @compare_dimension.setter
    def compare_dimension(self, compare_dimension):
        r"""Sets the compare_dimension of this CustomReportListVo.

        对比维度

        :param compare_dimension: The compare_dimension of this CustomReportListVo.
        :type compare_dimension: str
        """
        self._compare_dimension = compare_dimension

    @property
    def chart_data(self):
        r"""Gets the chart_data of this CustomReportListVo.

        报表数据

        :return: The chart_data of this CustomReportListVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ReportChartDataVo`]
        """
        return self._chart_data

    @chart_data.setter
    def chart_data(self, chart_data):
        r"""Sets the chart_data of this CustomReportListVo.

        报表数据

        :param chart_data: The chart_data of this CustomReportListVo.
        :type chart_data: list[:class:`huaweicloudsdkcloudtest.v1.ReportChartDataVo`]
        """
        self._chart_data = chart_data

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
        if not isinstance(other, CustomReportListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
