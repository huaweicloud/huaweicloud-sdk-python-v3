# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeSiteMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'dim': 'str'
    }

    attribute_map = {
        'site_id': 'site_id',
        'dim': 'dim'
    }

    def __init__(self, site_id=None, dim=None):
        """ListEdgeSiteMetricsRequest

        The model defined in huaweicloud sdk

        :param site_id: 边缘小站ID
        :type site_id: str
        :param dim: 指定维度查询 - site_id: 按站点维度，查询站点下计算、存储资源容量信息 - flavor: 按规格维度，查询站点下各flavor的计算资源使用情况 - storage: 按存储维度，查询站点下各存储资源类型的使用情况 - flavor_capacity: 按规格容量维度，查询站点下各规格可发放数量预测
        :type dim: str
        """
        
        

        self._site_id = None
        self._dim = None
        self.discriminator = None

        self.site_id = site_id
        if dim is not None:
            self.dim = dim

    @property
    def site_id(self):
        """Gets the site_id of this ListEdgeSiteMetricsRequest.

        边缘小站ID

        :return: The site_id of this ListEdgeSiteMetricsRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ListEdgeSiteMetricsRequest.

        边缘小站ID

        :param site_id: The site_id of this ListEdgeSiteMetricsRequest.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def dim(self):
        """Gets the dim of this ListEdgeSiteMetricsRequest.

        指定维度查询 - site_id: 按站点维度，查询站点下计算、存储资源容量信息 - flavor: 按规格维度，查询站点下各flavor的计算资源使用情况 - storage: 按存储维度，查询站点下各存储资源类型的使用情况 - flavor_capacity: 按规格容量维度，查询站点下各规格可发放数量预测

        :return: The dim of this ListEdgeSiteMetricsRequest.
        :rtype: str
        """
        return self._dim

    @dim.setter
    def dim(self, dim):
        """Sets the dim of this ListEdgeSiteMetricsRequest.

        指定维度查询 - site_id: 按站点维度，查询站点下计算、存储资源容量信息 - flavor: 按规格维度，查询站点下各flavor的计算资源使用情况 - storage: 按存储维度，查询站点下各存储资源类型的使用情况 - flavor_capacity: 按规格容量维度，查询站点下各规格可发放数量预测

        :param dim: The dim of this ListEdgeSiteMetricsRequest.
        :type dim: str
        """
        self._dim = dim

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
        if not isinstance(other, ListEdgeSiteMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
