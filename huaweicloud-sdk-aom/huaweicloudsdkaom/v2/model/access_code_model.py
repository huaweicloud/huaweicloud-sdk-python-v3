# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessCodeModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_code': 'str',
        'access_code_id': 'str',
        'create_at': 'int',
        'status': 'str'
    }

    attribute_map = {
        'access_code': 'access_code',
        'access_code_id': 'access_code_id',
        'create_at': 'create_at',
        'status': 'status'
    }

    def __init__(self, access_code=None, access_code_id=None, create_at=None, status=None):
        """AccessCodeModel

        The model defined in huaweicloud sdk

        :param access_code: access_code。
        :type access_code: str
        :param access_code_id: access_code_id。
        :type access_code_id: str
        :param create_at: 创建时间。
        :type create_at: int
        :param status: 状态。
        :type status: str
        """
        
        

        self._access_code = None
        self._access_code_id = None
        self._create_at = None
        self._status = None
        self.discriminator = None

        if access_code is not None:
            self.access_code = access_code
        if access_code_id is not None:
            self.access_code_id = access_code_id
        if create_at is not None:
            self.create_at = create_at
        if status is not None:
            self.status = status

    @property
    def access_code(self):
        """Gets the access_code of this AccessCodeModel.

        access_code。

        :return: The access_code of this AccessCodeModel.
        :rtype: str
        """
        return self._access_code

    @access_code.setter
    def access_code(self, access_code):
        """Sets the access_code of this AccessCodeModel.

        access_code。

        :param access_code: The access_code of this AccessCodeModel.
        :type access_code: str
        """
        self._access_code = access_code

    @property
    def access_code_id(self):
        """Gets the access_code_id of this AccessCodeModel.

        access_code_id。

        :return: The access_code_id of this AccessCodeModel.
        :rtype: str
        """
        return self._access_code_id

    @access_code_id.setter
    def access_code_id(self, access_code_id):
        """Sets the access_code_id of this AccessCodeModel.

        access_code_id。

        :param access_code_id: The access_code_id of this AccessCodeModel.
        :type access_code_id: str
        """
        self._access_code_id = access_code_id

    @property
    def create_at(self):
        """Gets the create_at of this AccessCodeModel.

        创建时间。

        :return: The create_at of this AccessCodeModel.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this AccessCodeModel.

        创建时间。

        :param create_at: The create_at of this AccessCodeModel.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def status(self):
        """Gets the status of this AccessCodeModel.

        状态。

        :return: The status of this AccessCodeModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccessCodeModel.

        状态。

        :param status: The status of this AccessCodeModel.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, AccessCodeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
