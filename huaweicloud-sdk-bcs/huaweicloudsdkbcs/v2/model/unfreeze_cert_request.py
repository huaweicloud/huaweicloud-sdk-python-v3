# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnfreezeCertRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'blockchain_id': 'str',
        'org_name': 'str',
        'body': 'UnfreezeCertRequestBody'
    }

    attribute_map = {
        'user_name': 'user_name',
        'blockchain_id': 'blockchain_id',
        'org_name': 'org_name',
        'body': 'body'
    }

    def __init__(self, user_name=None, blockchain_id=None, org_name=None, body=None):
        r"""UnfreezeCertRequest

        The model defined in huaweicloud sdk

        :param user_name: userName
        :type user_name: str
        :param blockchain_id: blockchainID
        :type blockchain_id: str
        :param org_name: orgName
        :type org_name: str
        :param body: Body of the UnfreezeCertRequest
        :type body: :class:`huaweicloudsdkbcs.v2.UnfreezeCertRequestBody`
        """
        
        

        self._user_name = None
        self._blockchain_id = None
        self._org_name = None
        self._body = None
        self.discriminator = None

        self.user_name = user_name
        self.blockchain_id = blockchain_id
        self.org_name = org_name
        if body is not None:
            self.body = body

    @property
    def user_name(self):
        r"""Gets the user_name of this UnfreezeCertRequest.

        userName

        :return: The user_name of this UnfreezeCertRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UnfreezeCertRequest.

        userName

        :param user_name: The user_name of this UnfreezeCertRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def blockchain_id(self):
        r"""Gets the blockchain_id of this UnfreezeCertRequest.

        blockchainID

        :return: The blockchain_id of this UnfreezeCertRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        r"""Sets the blockchain_id of this UnfreezeCertRequest.

        blockchainID

        :param blockchain_id: The blockchain_id of this UnfreezeCertRequest.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def org_name(self):
        r"""Gets the org_name of this UnfreezeCertRequest.

        orgName

        :return: The org_name of this UnfreezeCertRequest.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        r"""Sets the org_name of this UnfreezeCertRequest.

        orgName

        :param org_name: The org_name of this UnfreezeCertRequest.
        :type org_name: str
        """
        self._org_name = org_name

    @property
    def body(self):
        r"""Gets the body of this UnfreezeCertRequest.

        :return: The body of this UnfreezeCertRequest.
        :rtype: :class:`huaweicloudsdkbcs.v2.UnfreezeCertRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UnfreezeCertRequest.

        :param body: The body of this UnfreezeCertRequest.
        :type body: :class:`huaweicloudsdkbcs.v2.UnfreezeCertRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UnfreezeCertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
