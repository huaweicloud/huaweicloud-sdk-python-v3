# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalAttachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'doc_id': 'str',
        'doc_name': 'str'
    }

    attribute_map = {
        'doc_id': 'doc_id',
        'doc_name': 'doc_name'
    }

    def __init__(self, doc_id=None, doc_name=None):
        r"""ExternalAttachment

        The model defined in huaweicloud sdk

        :param doc_id: 附件唯一id。
        :type doc_id: str
        :param doc_name: 附件文件名。
        :type doc_name: str
        """
        
        

        self._doc_id = None
        self._doc_name = None
        self.discriminator = None

        if doc_id is not None:
            self.doc_id = doc_id
        if doc_name is not None:
            self.doc_name = doc_name

    @property
    def doc_id(self):
        r"""Gets the doc_id of this ExternalAttachment.

        附件唯一id。

        :return: The doc_id of this ExternalAttachment.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        r"""Sets the doc_id of this ExternalAttachment.

        附件唯一id。

        :param doc_id: The doc_id of this ExternalAttachment.
        :type doc_id: str
        """
        self._doc_id = doc_id

    @property
    def doc_name(self):
        r"""Gets the doc_name of this ExternalAttachment.

        附件文件名。

        :return: The doc_name of this ExternalAttachment.
        :rtype: str
        """
        return self._doc_name

    @doc_name.setter
    def doc_name(self, doc_name):
        r"""Sets the doc_name of this ExternalAttachment.

        附件文件名。

        :param doc_name: The doc_name of this ExternalAttachment.
        :type doc_name: str
        """
        self._doc_name = doc_name

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
        if not isinstance(other, ExternalAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
