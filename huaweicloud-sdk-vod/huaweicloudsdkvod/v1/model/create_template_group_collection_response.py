# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateGroupCollectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_collection_id': 'str'
    }

    attribute_map = {
        'group_collection_id': 'group_collection_id'
    }

    def __init__(self, group_collection_id=None):
        r"""CreateTemplateGroupCollectionResponse

        The model defined in huaweicloud sdk

        :param group_collection_id: 模板组集合ID&lt;br/&gt; 
        :type group_collection_id: str
        """
        
        super(CreateTemplateGroupCollectionResponse, self).__init__()

        self._group_collection_id = None
        self.discriminator = None

        if group_collection_id is not None:
            self.group_collection_id = group_collection_id

    @property
    def group_collection_id(self):
        r"""Gets the group_collection_id of this CreateTemplateGroupCollectionResponse.

        模板组集合ID<br/> 

        :return: The group_collection_id of this CreateTemplateGroupCollectionResponse.
        :rtype: str
        """
        return self._group_collection_id

    @group_collection_id.setter
    def group_collection_id(self, group_collection_id):
        r"""Sets the group_collection_id of this CreateTemplateGroupCollectionResponse.

        模板组集合ID<br/> 

        :param group_collection_id: The group_collection_id of this CreateTemplateGroupCollectionResponse.
        :type group_collection_id: str
        """
        self._group_collection_id = group_collection_id

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
        if not isinstance(other, CreateTemplateGroupCollectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
