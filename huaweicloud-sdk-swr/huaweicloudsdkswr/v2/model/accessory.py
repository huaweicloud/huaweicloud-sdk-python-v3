# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Accessory:

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
        'artifact_id': 'int',
        'subject_artifact_id': 'int',
        'size': 'int',
        'digest': 'str',
        'type': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'artifact_id': 'artifact_id',
        'subject_artifact_id': 'subject_artifact_id',
        'size': 'size',
        'digest': 'digest',
        'type': 'type',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, artifact_id=None, subject_artifact_id=None, size=None, digest=None, type=None, created_at=None):
        r"""Accessory

        The model defined in huaweicloud sdk

        :param id: 附件ID
        :type id: int
        :param artifact_id: 附件制品ID
        :type artifact_id: int
        :param subject_artifact_id: 附件所属制品ID.
        :type subject_artifact_id: int
        :param size: 附件的大小
        :type size: int
        :param digest: 附件的sha256值
        :type digest: str
        :param type: 附件的类型
        :type type: str
        :param created_at: 附件的创建时间
        :type created_at: datetime
        """
        
        

        self._id = None
        self._artifact_id = None
        self._subject_artifact_id = None
        self._size = None
        self._digest = None
        self._type = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if artifact_id is not None:
            self.artifact_id = artifact_id
        if subject_artifact_id is not None:
            self.subject_artifact_id = subject_artifact_id
        if size is not None:
            self.size = size
        if digest is not None:
            self.digest = digest
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this Accessory.

        附件ID

        :return: The id of this Accessory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Accessory.

        附件ID

        :param id: The id of this Accessory.
        :type id: int
        """
        self._id = id

    @property
    def artifact_id(self):
        r"""Gets the artifact_id of this Accessory.

        附件制品ID

        :return: The artifact_id of this Accessory.
        :rtype: int
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        r"""Sets the artifact_id of this Accessory.

        附件制品ID

        :param artifact_id: The artifact_id of this Accessory.
        :type artifact_id: int
        """
        self._artifact_id = artifact_id

    @property
    def subject_artifact_id(self):
        r"""Gets the subject_artifact_id of this Accessory.

        附件所属制品ID.

        :return: The subject_artifact_id of this Accessory.
        :rtype: int
        """
        return self._subject_artifact_id

    @subject_artifact_id.setter
    def subject_artifact_id(self, subject_artifact_id):
        r"""Sets the subject_artifact_id of this Accessory.

        附件所属制品ID.

        :param subject_artifact_id: The subject_artifact_id of this Accessory.
        :type subject_artifact_id: int
        """
        self._subject_artifact_id = subject_artifact_id

    @property
    def size(self):
        r"""Gets the size of this Accessory.

        附件的大小

        :return: The size of this Accessory.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Accessory.

        附件的大小

        :param size: The size of this Accessory.
        :type size: int
        """
        self._size = size

    @property
    def digest(self):
        r"""Gets the digest of this Accessory.

        附件的sha256值

        :return: The digest of this Accessory.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this Accessory.

        附件的sha256值

        :param digest: The digest of this Accessory.
        :type digest: str
        """
        self._digest = digest

    @property
    def type(self):
        r"""Gets the type of this Accessory.

        附件的类型

        :return: The type of this Accessory.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Accessory.

        附件的类型

        :param type: The type of this Accessory.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        r"""Gets the created_at of this Accessory.

        附件的创建时间

        :return: The created_at of this Accessory.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Accessory.

        附件的创建时间

        :param created_at: The created_at of this Accessory.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, Accessory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
