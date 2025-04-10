# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadProcessJsonDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'status': 'int',
        'cause': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'cause': 'cause'
    }

    def __init__(self, id=None, name=None, status=None, cause=None):
        r"""UploadProcessJsonDetail

        The model defined in huaweicloud sdk

        :param id: 导入进度Id
        :type id: int
        :param name: 工程名称
        :type name: str
        :param status: 导入状态（0：导入中；1：成功；2：失败）
        :type status: int
        :param cause: 失败原因
        :type cause: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._cause = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if cause is not None:
            self.cause = cause

    @property
    def id(self):
        r"""Gets the id of this UploadProcessJsonDetail.

        导入进度Id

        :return: The id of this UploadProcessJsonDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UploadProcessJsonDetail.

        导入进度Id

        :param id: The id of this UploadProcessJsonDetail.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UploadProcessJsonDetail.

        工程名称

        :return: The name of this UploadProcessJsonDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UploadProcessJsonDetail.

        工程名称

        :param name: The name of this UploadProcessJsonDetail.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this UploadProcessJsonDetail.

        导入状态（0：导入中；1：成功；2：失败）

        :return: The status of this UploadProcessJsonDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UploadProcessJsonDetail.

        导入状态（0：导入中；1：成功；2：失败）

        :param status: The status of this UploadProcessJsonDetail.
        :type status: int
        """
        self._status = status

    @property
    def cause(self):
        r"""Gets the cause of this UploadProcessJsonDetail.

        失败原因

        :return: The cause of this UploadProcessJsonDetail.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        r"""Sets the cause of this UploadProcessJsonDetail.

        失败原因

        :param cause: The cause of this UploadProcessJsonDetail.
        :type cause: str
        """
        self._cause = cause

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
        if not isinstance(other, UploadProcessJsonDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
