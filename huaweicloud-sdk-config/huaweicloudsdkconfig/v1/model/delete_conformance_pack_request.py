# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConformancePackRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conformance_pack_id': 'str'
    }

    attribute_map = {
        'conformance_pack_id': 'conformance_pack_id'
    }

    def __init__(self, conformance_pack_id=None):
        r"""DeleteConformancePackRequest

        The model defined in huaweicloud sdk

        :param conformance_pack_id: 合规规则包ID。
        :type conformance_pack_id: str
        """
        
        

        self._conformance_pack_id = None
        self.discriminator = None

        self.conformance_pack_id = conformance_pack_id

    @property
    def conformance_pack_id(self):
        r"""Gets the conformance_pack_id of this DeleteConformancePackRequest.

        合规规则包ID。

        :return: The conformance_pack_id of this DeleteConformancePackRequest.
        :rtype: str
        """
        return self._conformance_pack_id

    @conformance_pack_id.setter
    def conformance_pack_id(self, conformance_pack_id):
        r"""Sets the conformance_pack_id of this DeleteConformancePackRequest.

        合规规则包ID。

        :param conformance_pack_id: The conformance_pack_id of this DeleteConformancePackRequest.
        :type conformance_pack_id: str
        """
        self._conformance_pack_id = conformance_pack_id

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
        if not isinstance(other, DeleteConformancePackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
