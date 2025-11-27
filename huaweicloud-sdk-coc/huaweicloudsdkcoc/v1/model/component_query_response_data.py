# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentQueryResponseData:

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
        'name': 'str',
        'code': 'str',
        'domain_id': 'str',
        'application_id': 'str',
        'ep_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'domain_id': 'domain_id',
        'application_id': 'application_id',
        'ep_id': 'ep_id'
    }

    def __init__(self, id=None, name=None, code=None, domain_id=None, application_id=None, ep_id=None):
        r"""ComponentQueryResponseData

        The model defined in huaweicloud sdk

        :param id: CMDB分配的uuid。
        :type id: str
        :param name: 名称。
        :type name: str
        :param code: code。
        :type code: str
        :param domain_id: 租户id。
        :type domain_id: str
        :param application_id: 应用id。
        :type application_id: str
        :param ep_id: 企业项目id。
        :type ep_id: str
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._domain_id = None
        self._application_id = None
        self._ep_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if domain_id is not None:
            self.domain_id = domain_id
        if application_id is not None:
            self.application_id = application_id
        if ep_id is not None:
            self.ep_id = ep_id

    @property
    def id(self):
        r"""Gets the id of this ComponentQueryResponseData.

        CMDB分配的uuid。

        :return: The id of this ComponentQueryResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentQueryResponseData.

        CMDB分配的uuid。

        :param id: The id of this ComponentQueryResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ComponentQueryResponseData.

        名称。

        :return: The name of this ComponentQueryResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentQueryResponseData.

        名称。

        :param name: The name of this ComponentQueryResponseData.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this ComponentQueryResponseData.

        code。

        :return: The code of this ComponentQueryResponseData.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ComponentQueryResponseData.

        code。

        :param code: The code of this ComponentQueryResponseData.
        :type code: str
        """
        self._code = code

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ComponentQueryResponseData.

        租户id。

        :return: The domain_id of this ComponentQueryResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ComponentQueryResponseData.

        租户id。

        :param domain_id: The domain_id of this ComponentQueryResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def application_id(self):
        r"""Gets the application_id of this ComponentQueryResponseData.

        应用id。

        :return: The application_id of this ComponentQueryResponseData.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ComponentQueryResponseData.

        应用id。

        :param application_id: The application_id of this ComponentQueryResponseData.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ComponentQueryResponseData.

        企业项目id。

        :return: The ep_id of this ComponentQueryResponseData.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ComponentQueryResponseData.

        企业项目id。

        :param ep_id: The ep_id of this ComponentQueryResponseData.
        :type ep_id: str
        """
        self._ep_id = ep_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComponentQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
