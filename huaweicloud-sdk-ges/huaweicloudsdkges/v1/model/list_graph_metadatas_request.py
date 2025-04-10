# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphMetadatasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata_id': 'str'
    }

    attribute_map = {
        'metadata_id': 'metadata_id'
    }

    def __init__(self, metadata_id=None):
        r"""ListGraphMetadatasRequest

        The model defined in huaweicloud sdk

        :param metadata_id: 元数据ID。
        :type metadata_id: str
        """
        
        

        self._metadata_id = None
        self.discriminator = None

        self.metadata_id = metadata_id

    @property
    def metadata_id(self):
        r"""Gets the metadata_id of this ListGraphMetadatasRequest.

        元数据ID。

        :return: The metadata_id of this ListGraphMetadatasRequest.
        :rtype: str
        """
        return self._metadata_id

    @metadata_id.setter
    def metadata_id(self, metadata_id):
        r"""Sets the metadata_id of this ListGraphMetadatasRequest.

        元数据ID。

        :param metadata_id: The metadata_id of this ListGraphMetadatasRequest.
        :type metadata_id: str
        """
        self._metadata_id = metadata_id

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
        if not isinstance(other, ListGraphMetadatasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
