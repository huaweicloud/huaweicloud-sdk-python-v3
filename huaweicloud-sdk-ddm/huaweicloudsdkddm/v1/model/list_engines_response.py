# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnginesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'engine_groups': 'list[EngineGroupsInfo]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'engine_groups': 'engineGroups',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, engine_groups=None, offset=None, limit=None, total=None):
        """ListEnginesResponse - a model defined in huaweicloud sdk"""
        
        super(ListEnginesResponse, self).__init__()

        self._engine_groups = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if engine_groups is not None:
            self.engine_groups = engine_groups
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def engine_groups(self):
        """Gets the engine_groups of this ListEnginesResponse.

        引擎信息列表。

        :return: The engine_groups of this ListEnginesResponse.
        :rtype: list[EngineGroupsInfo]
        """
        return self._engine_groups

    @engine_groups.setter
    def engine_groups(self, engine_groups):
        """Sets the engine_groups of this ListEnginesResponse.

        引擎信息列表。

        :param engine_groups: The engine_groups of this ListEnginesResponse.
        :type: list[EngineGroupsInfo]
        """
        self._engine_groups = engine_groups

    @property
    def offset(self):
        """Gets the offset of this ListEnginesResponse.

        分页参数: 起始值。

        :return: The offset of this ListEnginesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnginesResponse.

        分页参数: 起始值。

        :param offset: The offset of this ListEnginesResponse.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEnginesResponse.

        分页参数：每页多少条。

        :return: The limit of this ListEnginesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnginesResponse.

        分页参数：每页多少条。

        :param limit: The limit of this ListEnginesResponse.
        :type: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this ListEnginesResponse.

        引擎信息总数。

        :return: The total of this ListEnginesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListEnginesResponse.

        引擎信息总数。

        :param total: The total of this ListEnginesResponse.
        :type: int
        """
        self._total = total

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListEnginesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other