# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDocumentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'document_id': 'str',
        'version': 'str',
        'document_type': 'str'
    }

    attribute_map = {
        'document_id': 'document_id',
        'version': 'version',
        'document_type': 'document_type'
    }

    def __init__(self, document_id=None, version=None, document_type=None):
        r"""GetDocumentRequest

        The model defined in huaweicloud sdk

        :param document_id: 作业uuid
        :type document_id: str
        :param version: 作业版本号，示例值v1、v2，不传默认查询最新版本
        :type version: str
        :param document_type: 执行的作业类型 枚举：PUBLIC/PRIVATE 默认PRIVATE
        :type document_type: str
        """
        
        

        self._document_id = None
        self._version = None
        self._document_type = None
        self.discriminator = None

        self.document_id = document_id
        if version is not None:
            self.version = version
        if document_type is not None:
            self.document_type = document_type

    @property
    def document_id(self):
        r"""Gets the document_id of this GetDocumentRequest.

        作业uuid

        :return: The document_id of this GetDocumentRequest.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this GetDocumentRequest.

        作业uuid

        :param document_id: The document_id of this GetDocumentRequest.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def version(self):
        r"""Gets the version of this GetDocumentRequest.

        作业版本号，示例值v1、v2，不传默认查询最新版本

        :return: The version of this GetDocumentRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this GetDocumentRequest.

        作业版本号，示例值v1、v2，不传默认查询最新版本

        :param version: The version of this GetDocumentRequest.
        :type version: str
        """
        self._version = version

    @property
    def document_type(self):
        r"""Gets the document_type of this GetDocumentRequest.

        执行的作业类型 枚举：PUBLIC/PRIVATE 默认PRIVATE

        :return: The document_type of this GetDocumentRequest.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        r"""Sets the document_type of this GetDocumentRequest.

        执行的作业类型 枚举：PUBLIC/PRIVATE 默认PRIVATE

        :param document_type: The document_type of this GetDocumentRequest.
        :type document_type: str
        """
        self._document_type = document_type

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
        if not isinstance(other, GetDocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
