# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEntityInfoByGuidResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity': 'OpenEntityWithExtInfoEntity',
        'referred_entities': 'object'
    }

    attribute_map = {
        'entity': 'entity',
        'referred_entities': 'referred_entities'
    }

    def __init__(self, entity=None, referred_entities=None):
        r"""ShowEntityInfoByGuidResponse

        The model defined in huaweicloud sdk

        :param entity: 
        :type entity: :class:`huaweicloudsdkdataartsstudio.v1.OpenEntityWithExtInfoEntity`
        :param referred_entities: 引用实体 Map&lt;String, OpenEntity&gt;
        :type referred_entities: object
        """
        
        super(ShowEntityInfoByGuidResponse, self).__init__()

        self._entity = None
        self._referred_entities = None
        self.discriminator = None

        if entity is not None:
            self.entity = entity
        if referred_entities is not None:
            self.referred_entities = referred_entities

    @property
    def entity(self):
        r"""Gets the entity of this ShowEntityInfoByGuidResponse.

        :return: The entity of this ShowEntityInfoByGuidResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.OpenEntityWithExtInfoEntity`
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        r"""Sets the entity of this ShowEntityInfoByGuidResponse.

        :param entity: The entity of this ShowEntityInfoByGuidResponse.
        :type entity: :class:`huaweicloudsdkdataartsstudio.v1.OpenEntityWithExtInfoEntity`
        """
        self._entity = entity

    @property
    def referred_entities(self):
        r"""Gets the referred_entities of this ShowEntityInfoByGuidResponse.

        引用实体 Map<String, OpenEntity>

        :return: The referred_entities of this ShowEntityInfoByGuidResponse.
        :rtype: object
        """
        return self._referred_entities

    @referred_entities.setter
    def referred_entities(self, referred_entities):
        r"""Sets the referred_entities of this ShowEntityInfoByGuidResponse.

        引用实体 Map<String, OpenEntity>

        :param referred_entities: The referred_entities of this ShowEntityInfoByGuidResponse.
        :type referred_entities: object
        """
        self._referred_entities = referred_entities

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
        if not isinstance(other, ShowEntityInfoByGuidResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
