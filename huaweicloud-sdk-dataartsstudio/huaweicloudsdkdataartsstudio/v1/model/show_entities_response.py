# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEntitiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'entities': 'list[OpenEntityHeader]',
        'scroll_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'entities': 'entities',
        'scroll_id': 'scroll_id'
    }

    def __init__(self, count=None, entities=None, scroll_id=None):
        r"""ShowEntitiesResponse

        The model defined in huaweicloud sdk

        :param count: 技术资产总数
        :type count: int
        :param entities: 技术资产列表
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenEntityHeader`]
        :param scroll_id: scroll_id
        :type scroll_id: str
        """
        
        super(ShowEntitiesResponse, self).__init__()

        self._count = None
        self._entities = None
        self._scroll_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if entities is not None:
            self.entities = entities
        if scroll_id is not None:
            self.scroll_id = scroll_id

    @property
    def count(self):
        r"""Gets the count of this ShowEntitiesResponse.

        技术资产总数

        :return: The count of this ShowEntitiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowEntitiesResponse.

        技术资产总数

        :param count: The count of this ShowEntitiesResponse.
        :type count: int
        """
        self._count = count

    @property
    def entities(self):
        r"""Gets the entities of this ShowEntitiesResponse.

        技术资产列表

        :return: The entities of this ShowEntitiesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenEntityHeader`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        r"""Sets the entities of this ShowEntitiesResponse.

        技术资产列表

        :param entities: The entities of this ShowEntitiesResponse.
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenEntityHeader`]
        """
        self._entities = entities

    @property
    def scroll_id(self):
        r"""Gets the scroll_id of this ShowEntitiesResponse.

        scroll_id

        :return: The scroll_id of this ShowEntitiesResponse.
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        r"""Sets the scroll_id of this ShowEntitiesResponse.

        scroll_id

        :param scroll_id: The scroll_id of this ShowEntitiesResponse.
        :type scroll_id: str
        """
        self._scroll_id = scroll_id

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
        if not isinstance(other, ShowEntitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
