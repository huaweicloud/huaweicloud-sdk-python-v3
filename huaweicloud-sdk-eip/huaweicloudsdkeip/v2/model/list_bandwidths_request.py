# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'enterprise_project_id': 'str',
        'share_type': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'enterprise_project_id': 'enterprise_project_id',
        'share_type': 'share_type'
    }

    def __init__(self, marker=None, limit=None, enterprise_project_id=None, share_type=None):
        """ListBandwidthsRequest

        The model defined in huaweicloud sdk

        :param marker: 取值为上一页数据的最后一条记录的id，为空时为查询第一页
        :type marker: str
        :param limit: 功能说明：每页返回的个数  取值范围：0~intmax
        :type limit: int
        :param enterprise_project_id: 功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的虚拟私有云。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的虚拟私有云，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param share_type: 功能说明：带宽类型，标识是否是共享带宽 取值范围：WHOLE，PER WHOLE表示共享带宽；PER，表示独享带宽
        :type share_type: str
        """
        
        

        self._marker = None
        self._limit = None
        self._enterprise_project_id = None
        self._share_type = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if share_type is not None:
            self.share_type = share_type

    @property
    def marker(self):
        """Gets the marker of this ListBandwidthsRequest.

        取值为上一页数据的最后一条记录的id，为空时为查询第一页

        :return: The marker of this ListBandwidthsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListBandwidthsRequest.

        取值为上一页数据的最后一条记录的id，为空时为查询第一页

        :param marker: The marker of this ListBandwidthsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListBandwidthsRequest.

        功能说明：每页返回的个数  取值范围：0~intmax

        :return: The limit of this ListBandwidthsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBandwidthsRequest.

        功能说明：每页返回的个数  取值范围：0~intmax

        :param limit: The limit of this ListBandwidthsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListBandwidthsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的虚拟私有云。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的虚拟私有云，请传参all_granted_eps。

        :return: The enterprise_project_id of this ListBandwidthsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListBandwidthsRequest.

        功能说明：企业项目ID。可以使用该字段过滤某个企业项目下的虚拟私有云。  取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。若需要查询当前用户所有企业项目绑定的虚拟私有云，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this ListBandwidthsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def share_type(self):
        """Gets the share_type of this ListBandwidthsRequest.

        功能说明：带宽类型，标识是否是共享带宽 取值范围：WHOLE，PER WHOLE表示共享带宽；PER，表示独享带宽

        :return: The share_type of this ListBandwidthsRequest.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this ListBandwidthsRequest.

        功能说明：带宽类型，标识是否是共享带宽 取值范围：WHOLE，PER WHOLE表示共享带宽；PER，表示独享带宽

        :param share_type: The share_type of this ListBandwidthsRequest.
        :type share_type: str
        """
        self._share_type = share_type

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
        if not isinstance(other, ListBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
