# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagVO:

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
        'description': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'new_biz': 'BizVersionManageVO'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'new_biz': 'new_biz'
    }

    def __init__(self, id=None, name=None, description=None, create_by=None, update_by=None, create_time=None, update_time=None, new_biz=None):
        """TagVO

        The model defined in huaweicloud sdk

        :param id: 编码，填写String类型替代Long类型。
        :type id: str
        :param name: 标签名。
        :type name: str
        :param description: 描述。
        :type description: str
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self._new_biz = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if new_biz is not None:
            self.new_biz = new_biz

    @property
    def id(self):
        """Gets the id of this TagVO.

        编码，填写String类型替代Long类型。

        :return: The id of this TagVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TagVO.

        编码，填写String类型替代Long类型。

        :param id: The id of this TagVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TagVO.

        标签名。

        :return: The name of this TagVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagVO.

        标签名。

        :param name: The name of this TagVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this TagVO.

        描述。

        :return: The description of this TagVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TagVO.

        描述。

        :param description: The description of this TagVO.
        :type description: str
        """
        self._description = description

    @property
    def create_by(self):
        """Gets the create_by of this TagVO.

        创建人。

        :return: The create_by of this TagVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this TagVO.

        创建人。

        :param create_by: The create_by of this TagVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this TagVO.

        更新人。

        :return: The update_by of this TagVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this TagVO.

        更新人。

        :param update_by: The update_by of this TagVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        """Gets the create_time of this TagVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this TagVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TagVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this TagVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this TagVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this TagVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TagVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this TagVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def new_biz(self):
        """Gets the new_biz of this TagVO.

        :return: The new_biz of this TagVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        """Sets the new_biz of this TagVO.

        :param new_biz: The new_biz of this TagVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

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
        if not isinstance(other, TagVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
