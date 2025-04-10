# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgreementVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'agreement_name': 'str',
        'agreement_type': 'str',
        'agreement_type_name': 'str',
        'content': 'str',
        'version': 'int'
    }

    attribute_map = {
        'id': 'id',
        'agreement_name': 'agreement_name',
        'agreement_type': 'agreement_type',
        'agreement_type_name': 'agreement_type_name',
        'content': 'content',
        'version': 'version'
    }

    def __init__(self, id=None, agreement_name=None, agreement_type=None, agreement_type_name=None, content=None, version=None):
        r"""AgreementVO

        The model defined in huaweicloud sdk

        :param id: 协议id
        :type id: str
        :param agreement_name: 协议名称
        :type agreement_name: str
        :param agreement_type: 协议类型
        :type agreement_type: str
        :param agreement_type_name: 协议类型名称
        :type agreement_type_name: str
        :param content: 内容
        :type content: str
        :param version: 版本
        :type version: int
        """
        
        

        self._id = None
        self._agreement_name = None
        self._agreement_type = None
        self._agreement_type_name = None
        self._content = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if agreement_name is not None:
            self.agreement_name = agreement_name
        if agreement_type is not None:
            self.agreement_type = agreement_type
        if agreement_type_name is not None:
            self.agreement_type_name = agreement_type_name
        if content is not None:
            self.content = content
        if version is not None:
            self.version = version

    @property
    def id(self):
        r"""Gets the id of this AgreementVO.

        协议id

        :return: The id of this AgreementVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AgreementVO.

        协议id

        :param id: The id of this AgreementVO.
        :type id: str
        """
        self._id = id

    @property
    def agreement_name(self):
        r"""Gets the agreement_name of this AgreementVO.

        协议名称

        :return: The agreement_name of this AgreementVO.
        :rtype: str
        """
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, agreement_name):
        r"""Sets the agreement_name of this AgreementVO.

        协议名称

        :param agreement_name: The agreement_name of this AgreementVO.
        :type agreement_name: str
        """
        self._agreement_name = agreement_name

    @property
    def agreement_type(self):
        r"""Gets the agreement_type of this AgreementVO.

        协议类型

        :return: The agreement_type of this AgreementVO.
        :rtype: str
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, agreement_type):
        r"""Sets the agreement_type of this AgreementVO.

        协议类型

        :param agreement_type: The agreement_type of this AgreementVO.
        :type agreement_type: str
        """
        self._agreement_type = agreement_type

    @property
    def agreement_type_name(self):
        r"""Gets the agreement_type_name of this AgreementVO.

        协议类型名称

        :return: The agreement_type_name of this AgreementVO.
        :rtype: str
        """
        return self._agreement_type_name

    @agreement_type_name.setter
    def agreement_type_name(self, agreement_type_name):
        r"""Sets the agreement_type_name of this AgreementVO.

        协议类型名称

        :param agreement_type_name: The agreement_type_name of this AgreementVO.
        :type agreement_type_name: str
        """
        self._agreement_type_name = agreement_type_name

    @property
    def content(self):
        r"""Gets the content of this AgreementVO.

        内容

        :return: The content of this AgreementVO.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this AgreementVO.

        内容

        :param content: The content of this AgreementVO.
        :type content: str
        """
        self._content = content

    @property
    def version(self):
        r"""Gets the version of this AgreementVO.

        版本

        :return: The version of this AgreementVO.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AgreementVO.

        版本

        :param version: The version of this AgreementVO.
        :type version: int
        """
        self._version = version

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
        if not isinstance(other, AgreementVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
