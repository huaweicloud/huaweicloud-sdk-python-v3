# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWarmPoolInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, scaling_group_id=None, limit=None, marker=None):
        r"""ListWarmPoolInstancesRequest

        The model defined in huaweicloud sdk

        :param scaling_group_id: 伸缩组ID
        :type scaling_group_id: str
        :param limit: 查询的记录条数，不传默认20，最大可传入100
        :type limit: int
        :param marker: 查询暖池实例的分页marker
        :type marker: str
        """
        
        

        self._scaling_group_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def scaling_group_id(self):
        r"""Gets the scaling_group_id of this ListWarmPoolInstancesRequest.

        伸缩组ID

        :return: The scaling_group_id of this ListWarmPoolInstancesRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        r"""Sets the scaling_group_id of this ListWarmPoolInstancesRequest.

        伸缩组ID

        :param scaling_group_id: The scaling_group_id of this ListWarmPoolInstancesRequest.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def limit(self):
        r"""Gets the limit of this ListWarmPoolInstancesRequest.

        查询的记录条数，不传默认20，最大可传入100

        :return: The limit of this ListWarmPoolInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWarmPoolInstancesRequest.

        查询的记录条数，不传默认20，最大可传入100

        :param limit: The limit of this ListWarmPoolInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListWarmPoolInstancesRequest.

        查询暖池实例的分页marker

        :return: The marker of this ListWarmPoolInstancesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListWarmPoolInstancesRequest.

        查询暖池实例的分页marker

        :param marker: The marker of this ListWarmPoolInstancesRequest.
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
        if not isinstance(other, ListWarmPoolInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
