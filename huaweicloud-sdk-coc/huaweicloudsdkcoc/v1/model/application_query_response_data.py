# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationQueryResponseData:

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
        'parent_id': 'str',
        'description': 'str',
        'path': 'str',
        'is_collection': 'bool',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'domain_id': 'domain_id',
        'parent_id': 'parent_id',
        'description': 'description',
        'path': 'path',
        'is_collection': 'is_collection',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, code=None, domain_id=None, parent_id=None, description=None, path=None, is_collection=None, create_time=None, update_time=None):
        r"""ApplicationQueryResponseData

        The model defined in huaweicloud sdk

        :param id: 应用id
        :type id: str
        :param name: 应用名称
        :type name: str
        :param code: 应用code
        :type code: str
        :param domain_id: 租户id
        :type domain_id: str
        :param parent_id: 父节点id
        :type parent_id: str
        :param description: 描述信息
        :type description: str
        :param path: 应用path路径，由应用id用.拼接
        :type path: str
        :param is_collection: 是否为收藏应用
        :type is_collection: bool
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._code = None
        self._domain_id = None
        self._parent_id = None
        self._description = None
        self._path = None
        self._is_collection = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if domain_id is not None:
            self.domain_id = domain_id
        if parent_id is not None:
            self.parent_id = parent_id
        if description is not None:
            self.description = description
        if path is not None:
            self.path = path
        if is_collection is not None:
            self.is_collection = is_collection
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ApplicationQueryResponseData.

        应用id

        :return: The id of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApplicationQueryResponseData.

        应用id

        :param id: The id of this ApplicationQueryResponseData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ApplicationQueryResponseData.

        应用名称

        :return: The name of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationQueryResponseData.

        应用名称

        :param name: The name of this ApplicationQueryResponseData.
        :type name: str
        """
        self._name = name

    @property
    def code(self):
        r"""Gets the code of this ApplicationQueryResponseData.

        应用code

        :return: The code of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ApplicationQueryResponseData.

        应用code

        :param code: The code of this ApplicationQueryResponseData.
        :type code: str
        """
        self._code = code

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ApplicationQueryResponseData.

        租户id

        :return: The domain_id of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ApplicationQueryResponseData.

        租户id

        :param domain_id: The domain_id of this ApplicationQueryResponseData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ApplicationQueryResponseData.

        父节点id

        :return: The parent_id of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ApplicationQueryResponseData.

        父节点id

        :param parent_id: The parent_id of this ApplicationQueryResponseData.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def description(self):
        r"""Gets the description of this ApplicationQueryResponseData.

        描述信息

        :return: The description of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApplicationQueryResponseData.

        描述信息

        :param description: The description of this ApplicationQueryResponseData.
        :type description: str
        """
        self._description = description

    @property
    def path(self):
        r"""Gets the path of this ApplicationQueryResponseData.

        应用path路径，由应用id用.拼接

        :return: The path of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ApplicationQueryResponseData.

        应用path路径，由应用id用.拼接

        :param path: The path of this ApplicationQueryResponseData.
        :type path: str
        """
        self._path = path

    @property
    def is_collection(self):
        r"""Gets the is_collection of this ApplicationQueryResponseData.

        是否为收藏应用

        :return: The is_collection of this ApplicationQueryResponseData.
        :rtype: bool
        """
        return self._is_collection

    @is_collection.setter
    def is_collection(self, is_collection):
        r"""Sets the is_collection of this ApplicationQueryResponseData.

        是否为收藏应用

        :param is_collection: The is_collection of this ApplicationQueryResponseData.
        :type is_collection: bool
        """
        self._is_collection = is_collection

    @property
    def create_time(self):
        r"""Gets the create_time of this ApplicationQueryResponseData.

        创建时间

        :return: The create_time of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ApplicationQueryResponseData.

        创建时间

        :param create_time: The create_time of this ApplicationQueryResponseData.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ApplicationQueryResponseData.

        修改时间

        :return: The update_time of this ApplicationQueryResponseData.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ApplicationQueryResponseData.

        修改时间

        :param update_time: The update_time of this ApplicationQueryResponseData.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ApplicationQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
