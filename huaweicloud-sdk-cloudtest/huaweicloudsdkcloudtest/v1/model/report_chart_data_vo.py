# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportChartDataVo:

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
        'analyze_dim': 'ReportDimVo',
        'compare_dim': 'list[ReportDimVo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'analyze_dim': 'analyze_dim',
        'compare_dim': 'compare_dim'
    }

    def __init__(self, id=None, name=None, analyze_dim=None, compare_dim=None):
        r"""ReportChartDataVo

        The model defined in huaweicloud sdk

        :param id: 报表id
        :type id: str
        :param name: 报表名称
        :type name: str
        :param analyze_dim: 
        :type analyze_dim: :class:`huaweicloudsdkcloudtest.v1.ReportDimVo`
        :param compare_dim: 对比维度数据
        :type compare_dim: list[:class:`huaweicloudsdkcloudtest.v1.ReportDimVo`]
        """
        
        

        self._id = None
        self._name = None
        self._analyze_dim = None
        self._compare_dim = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if analyze_dim is not None:
            self.analyze_dim = analyze_dim
        if compare_dim is not None:
            self.compare_dim = compare_dim

    @property
    def id(self):
        r"""Gets the id of this ReportChartDataVo.

        报表id

        :return: The id of this ReportChartDataVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReportChartDataVo.

        报表id

        :param id: The id of this ReportChartDataVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ReportChartDataVo.

        报表名称

        :return: The name of this ReportChartDataVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ReportChartDataVo.

        报表名称

        :param name: The name of this ReportChartDataVo.
        :type name: str
        """
        self._name = name

    @property
    def analyze_dim(self):
        r"""Gets the analyze_dim of this ReportChartDataVo.

        :return: The analyze_dim of this ReportChartDataVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ReportDimVo`
        """
        return self._analyze_dim

    @analyze_dim.setter
    def analyze_dim(self, analyze_dim):
        r"""Sets the analyze_dim of this ReportChartDataVo.

        :param analyze_dim: The analyze_dim of this ReportChartDataVo.
        :type analyze_dim: :class:`huaweicloudsdkcloudtest.v1.ReportDimVo`
        """
        self._analyze_dim = analyze_dim

    @property
    def compare_dim(self):
        r"""Gets the compare_dim of this ReportChartDataVo.

        对比维度数据

        :return: The compare_dim of this ReportChartDataVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ReportDimVo`]
        """
        return self._compare_dim

    @compare_dim.setter
    def compare_dim(self, compare_dim):
        r"""Sets the compare_dim of this ReportChartDataVo.

        对比维度数据

        :param compare_dim: The compare_dim of this ReportChartDataVo.
        :type compare_dim: list[:class:`huaweicloudsdkcloudtest.v1.ReportDimVo`]
        """
        self._compare_dim = compare_dim

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
        if not isinstance(other, ReportChartDataVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
