# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelRsp:

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
        'creator': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, creator=None, create_time=None, update_time=None):
        """LabelRsp

        The model defined in huaweicloud sdk

        :param id: 标签id
        :type id: str
        :param name: 标签名称
        :type name: str
        :param description: 标签描述
        :type description: str
        :param creator: 标签创建者
        :type creator: str
        :param create_time: 标签创建时间
        :type create_time: str
        :param update_time: 标签更新时间
        :type update_time: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this LabelRsp.

        标签id

        :return: The id of this LabelRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LabelRsp.

        标签id

        :param id: The id of this LabelRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this LabelRsp.

        标签名称

        :return: The name of this LabelRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelRsp.

        标签名称

        :param name: The name of this LabelRsp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this LabelRsp.

        标签描述

        :return: The description of this LabelRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LabelRsp.

        标签描述

        :param description: The description of this LabelRsp.
        :type description: str
        """
        self._description = description

    @property
    def creator(self):
        """Gets the creator of this LabelRsp.

        标签创建者

        :return: The creator of this LabelRsp.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this LabelRsp.

        标签创建者

        :param creator: The creator of this LabelRsp.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this LabelRsp.

        标签创建时间

        :return: The create_time of this LabelRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this LabelRsp.

        标签创建时间

        :param create_time: The create_time of this LabelRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this LabelRsp.

        标签更新时间

        :return: The update_time of this LabelRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this LabelRsp.

        标签更新时间

        :param update_time: The update_time of this LabelRsp.
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
        if not isinstance(other, LabelRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
