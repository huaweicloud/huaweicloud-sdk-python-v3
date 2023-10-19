# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, instance_id=None, limit=None, marker=None):
        """ListConfigsRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param limit: 查询返回条数。默认值为1000。最小值为0，最大值为1000。
        :type limit: int
        :param marker: 查询的起始记录ID。最小长度为0，最大长度为256。
        :type marker: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def instance_id(self):
        """Gets the instance_id of this ListConfigsRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListConfigsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListConfigsRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListConfigsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListConfigsRequest.

        查询返回条数。默认值为1000。最小值为0，最大值为1000。

        :return: The limit of this ListConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListConfigsRequest.

        查询返回条数。默认值为1000。最小值为0，最大值为1000。

        :param limit: The limit of this ListConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListConfigsRequest.

        查询的起始记录ID。最小长度为0，最大长度为256。

        :return: The marker of this ListConfigsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListConfigsRequest.

        查询的起始记录ID。最小长度为0，最大长度为256。

        :param marker: The marker of this ListConfigsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
