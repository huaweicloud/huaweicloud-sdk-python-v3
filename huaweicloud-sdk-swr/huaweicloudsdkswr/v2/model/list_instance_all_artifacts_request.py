# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceAllArtifactsRequest:

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
        'marker': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, marker=None, limit=None):
        r"""ListInstanceAllArtifactsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param marker: 分页查询时的查询标记，使用上一次接口调用返回的nextMarker值。默认值为1。**注意：marker和limit参数需要配套使用。**
        :type marker: int
        :param limit: 返回条数，默认为10，最大值为100。**注意：marker和limit参数需要配套使用。**
        :type limit: int
        """
        
        

        self._instance_id = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceAllArtifactsRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceAllArtifactsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceAllArtifactsRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceAllArtifactsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def marker(self):
        r"""Gets the marker of this ListInstanceAllArtifactsRequest.

        分页查询时的查询标记，使用上一次接口调用返回的nextMarker值。默认值为1。**注意：marker和limit参数需要配套使用。**

        :return: The marker of this ListInstanceAllArtifactsRequest.
        :rtype: int
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListInstanceAllArtifactsRequest.

        分页查询时的查询标记，使用上一次接口调用返回的nextMarker值。默认值为1。**注意：marker和limit参数需要配套使用。**

        :param marker: The marker of this ListInstanceAllArtifactsRequest.
        :type marker: int
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceAllArtifactsRequest.

        返回条数，默认为10，最大值为100。**注意：marker和limit参数需要配套使用。**

        :return: The limit of this ListInstanceAllArtifactsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceAllArtifactsRequest.

        返回条数，默认为10，最大值为100。**注意：marker和limit参数需要配套使用。**

        :param limit: The limit of this ListInstanceAllArtifactsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListInstanceAllArtifactsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
