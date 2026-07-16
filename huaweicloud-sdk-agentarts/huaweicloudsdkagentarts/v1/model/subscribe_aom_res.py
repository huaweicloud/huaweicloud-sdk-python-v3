# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeAomRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prom_id': 'str',
        'prom_name': 'str',
        'access_code': 'str',
        'access_code_id': 'str'
    }

    attribute_map = {
        'prom_id': 'prom_id',
        'prom_name': 'prom_name',
        'access_code': 'access_code',
        'access_code_id': 'access_code_id'
    }

    def __init__(self, prom_id=None, prom_name=None, access_code=None, access_code_id=None):
        r"""SubscribeAomRes

        The model defined in huaweicloud sdk

        :param prom_id: 普罗实例id
        :type prom_id: str
        :param prom_name: 普罗实例名称
        :type prom_name: str
        :param access_code: aom访问码
        :type access_code: str
        :param access_code_id: aom访问码id
        :type access_code_id: str
        """
        
        

        self._prom_id = None
        self._prom_name = None
        self._access_code = None
        self._access_code_id = None
        self.discriminator = None

        if prom_id is not None:
            self.prom_id = prom_id
        if prom_name is not None:
            self.prom_name = prom_name
        if access_code is not None:
            self.access_code = access_code
        if access_code_id is not None:
            self.access_code_id = access_code_id

    @property
    def prom_id(self):
        r"""Gets the prom_id of this SubscribeAomRes.

        普罗实例id

        :return: The prom_id of this SubscribeAomRes.
        :rtype: str
        """
        return self._prom_id

    @prom_id.setter
    def prom_id(self, prom_id):
        r"""Sets the prom_id of this SubscribeAomRes.

        普罗实例id

        :param prom_id: The prom_id of this SubscribeAomRes.
        :type prom_id: str
        """
        self._prom_id = prom_id

    @property
    def prom_name(self):
        r"""Gets the prom_name of this SubscribeAomRes.

        普罗实例名称

        :return: The prom_name of this SubscribeAomRes.
        :rtype: str
        """
        return self._prom_name

    @prom_name.setter
    def prom_name(self, prom_name):
        r"""Sets the prom_name of this SubscribeAomRes.

        普罗实例名称

        :param prom_name: The prom_name of this SubscribeAomRes.
        :type prom_name: str
        """
        self._prom_name = prom_name

    @property
    def access_code(self):
        r"""Gets the access_code of this SubscribeAomRes.

        aom访问码

        :return: The access_code of this SubscribeAomRes.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        r"""Sets the access_code of this SubscribeAomRes.

        aom访问码

        :param access_code: The access_code of this SubscribeAomRes.
        :type access_code: str
        """
        self._access_code = access_code

    @property
    def access_code_id(self):
        r"""Gets the access_code_id of this SubscribeAomRes.

        aom访问码id

        :return: The access_code_id of this SubscribeAomRes.
        :rtype: str
        """
        return self._access_code_id

    @access_code_id.setter
    def access_code_id(self, access_code_id):
        r"""Sets the access_code_id of this SubscribeAomRes.

        aom访问码id

        :param access_code_id: The access_code_id of this SubscribeAomRes.
        :type access_code_id: str
        """
        self._access_code_id = access_code_id

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
        if not isinstance(other, SubscribeAomRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
