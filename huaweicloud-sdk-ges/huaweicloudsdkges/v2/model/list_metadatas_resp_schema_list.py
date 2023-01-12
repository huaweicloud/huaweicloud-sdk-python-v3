# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetadatasRespSchemaList:

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
        'start_time': 'str',
        'last_update_time': 'str',
        'encrypted': 'bool',
        'master_key_name': 'str',
        'master_key_id': 'str',
        'description': 'str',
        'metadata_path': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_time': 'start_time',
        'last_update_time': 'last_update_time',
        'encrypted': 'encrypted',
        'master_key_name': 'master_key_name',
        'master_key_id': 'master_key_id',
        'description': 'description',
        'metadata_path': 'metadata_path',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, start_time=None, last_update_time=None, encrypted=None, master_key_name=None, master_key_id=None, description=None, metadata_path=None, status=None):
        """ListMetadatasRespSchemaList

        The model defined in huaweicloud sdk

        :param id: 元数据 ID。
        :type id: str
        :param name: 元数据名称。
        :type name: str
        :param start_time: 元数据创建时间
        :type start_time: str
        :param last_update_time: 元数据最后更新时间
        :type last_update_time: str
        :param encrypted: 元数据是否加密
        :type encrypted: bool
        :param master_key_name: 秘钥名称
        :type master_key_name: str
        :param master_key_id: 秘钥id
        :type master_key_id: str
        :param description: 元数据 描述。
        :type description: str
        :param metadata_path: 元数据对应路径。
        :type metadata_path: str
        :param status: 元数据是否可用。
        :type status: str
        """
        
        

        self._id = None
        self._name = None
        self._start_time = None
        self._last_update_time = None
        self._encrypted = None
        self._master_key_name = None
        self._master_key_id = None
        self._description = None
        self._metadata_path = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if start_time is not None:
            self.start_time = start_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if encrypted is not None:
            self.encrypted = encrypted
        if master_key_name is not None:
            self.master_key_name = master_key_name
        if master_key_id is not None:
            self.master_key_id = master_key_id
        if description is not None:
            self.description = description
        if metadata_path is not None:
            self.metadata_path = metadata_path
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ListMetadatasRespSchemaList.

        元数据 ID。

        :return: The id of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListMetadatasRespSchemaList.

        元数据 ID。

        :param id: The id of this ListMetadatasRespSchemaList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListMetadatasRespSchemaList.

        元数据名称。

        :return: The name of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListMetadatasRespSchemaList.

        元数据名称。

        :param name: The name of this ListMetadatasRespSchemaList.
        :type name: str
        """
        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this ListMetadatasRespSchemaList.

        元数据创建时间

        :return: The start_time of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListMetadatasRespSchemaList.

        元数据创建时间

        :param start_time: The start_time of this ListMetadatasRespSchemaList.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this ListMetadatasRespSchemaList.

        元数据最后更新时间

        :return: The last_update_time of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this ListMetadatasRespSchemaList.

        元数据最后更新时间

        :param last_update_time: The last_update_time of this ListMetadatasRespSchemaList.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def encrypted(self):
        """Gets the encrypted of this ListMetadatasRespSchemaList.

        元数据是否加密

        :return: The encrypted of this ListMetadatasRespSchemaList.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this ListMetadatasRespSchemaList.

        元数据是否加密

        :param encrypted: The encrypted of this ListMetadatasRespSchemaList.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def master_key_name(self):
        """Gets the master_key_name of this ListMetadatasRespSchemaList.

        秘钥名称

        :return: The master_key_name of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        """Sets the master_key_name of this ListMetadatasRespSchemaList.

        秘钥名称

        :param master_key_name: The master_key_name of this ListMetadatasRespSchemaList.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def master_key_id(self):
        """Gets the master_key_id of this ListMetadatasRespSchemaList.

        秘钥id

        :return: The master_key_id of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        """Sets the master_key_id of this ListMetadatasRespSchemaList.

        秘钥id

        :param master_key_id: The master_key_id of this ListMetadatasRespSchemaList.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

    @property
    def description(self):
        """Gets the description of this ListMetadatasRespSchemaList.

        元数据 描述。

        :return: The description of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListMetadatasRespSchemaList.

        元数据 描述。

        :param description: The description of this ListMetadatasRespSchemaList.
        :type description: str
        """
        self._description = description

    @property
    def metadata_path(self):
        """Gets the metadata_path of this ListMetadatasRespSchemaList.

        元数据对应路径。

        :return: The metadata_path of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._metadata_path

    @metadata_path.setter
    def metadata_path(self, metadata_path):
        """Sets the metadata_path of this ListMetadatasRespSchemaList.

        元数据对应路径。

        :param metadata_path: The metadata_path of this ListMetadatasRespSchemaList.
        :type metadata_path: str
        """
        self._metadata_path = metadata_path

    @property
    def status(self):
        """Gets the status of this ListMetadatasRespSchemaList.

        元数据是否可用。

        :return: The status of this ListMetadatasRespSchemaList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListMetadatasRespSchemaList.

        元数据是否可用。

        :param status: The status of this ListMetadatasRespSchemaList.
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
        if not isinstance(other, ListMetadatasRespSchemaList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
