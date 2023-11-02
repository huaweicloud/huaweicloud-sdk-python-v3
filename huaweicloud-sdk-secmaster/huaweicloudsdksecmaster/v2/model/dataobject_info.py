# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataobjectInfo:

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
        'create_time': 'str',
        'update_time': 'str',
        'project_id': 'str',
        'dataclass_id': 'str',
        'name': 'str',
        'content': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'project_id': 'project_id',
        'dataclass_id': 'dataclass_id',
        'name': 'name',
        'content': 'content'
    }

    def __init__(self, id=None, create_time=None, update_time=None, project_id=None, dataclass_id=None, name=None, content=None):
        """DataobjectInfo

        The model defined in huaweicloud sdk

        :param id: ID值
        :type id: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param project_id: 项目ID
        :type project_id: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param name: 名称
        :type name: str
        :param content: 数据内容
        :type content: str
        """
        
        

        self._id = None
        self._create_time = None
        self._update_time = None
        self._project_id = None
        self._dataclass_id = None
        self._name = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if project_id is not None:
            self.project_id = project_id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if name is not None:
            self.name = name
        if content is not None:
            self.content = content

    @property
    def id(self):
        """Gets the id of this DataobjectInfo.

        ID值

        :return: The id of this DataobjectInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataobjectInfo.

        ID值

        :param id: The id of this DataobjectInfo.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this DataobjectInfo.

        创建时间

        :return: The create_time of this DataobjectInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataobjectInfo.

        创建时间

        :param create_time: The create_time of this DataobjectInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DataobjectInfo.

        更新时间

        :return: The update_time of this DataobjectInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataobjectInfo.

        更新时间

        :param update_time: The update_time of this DataobjectInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        """Gets the project_id of this DataobjectInfo.

        项目ID

        :return: The project_id of this DataobjectInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DataobjectInfo.

        项目ID

        :param project_id: The project_id of this DataobjectInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this DataobjectInfo.

        数据类ID

        :return: The dataclass_id of this DataobjectInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this DataobjectInfo.

        数据类ID

        :param dataclass_id: The dataclass_id of this DataobjectInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def name(self):
        """Gets the name of this DataobjectInfo.

        名称

        :return: The name of this DataobjectInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataobjectInfo.

        名称

        :param name: The name of this DataobjectInfo.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        """Gets the content of this DataobjectInfo.

        数据内容

        :return: The content of this DataobjectInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DataobjectInfo.

        数据内容

        :param content: The content of this DataobjectInfo.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, DataobjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
