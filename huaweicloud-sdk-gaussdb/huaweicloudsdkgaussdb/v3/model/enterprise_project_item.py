# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseProjectItem:

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
        'status': 'str',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, description=None, status=None, created=None, updated=None):
        """EnterpriseProjectItem

        The model defined in huaweicloud sdk

        :param id: 企业项目ID。
        :type id: str
        :param name: 企业项目名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param status: 状态。 - 1：正常。 - 0：异常。
        :type status: str
        :param created: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type created: str
        :param updated: 更新时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type updated: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this EnterpriseProjectItem.

        企业项目ID。

        :return: The id of this EnterpriseProjectItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnterpriseProjectItem.

        企业项目ID。

        :param id: The id of this EnterpriseProjectItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EnterpriseProjectItem.

        企业项目名称。

        :return: The name of this EnterpriseProjectItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnterpriseProjectItem.

        企业项目名称。

        :param name: The name of this EnterpriseProjectItem.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EnterpriseProjectItem.

        描述。

        :return: The description of this EnterpriseProjectItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnterpriseProjectItem.

        描述。

        :param description: The description of this EnterpriseProjectItem.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this EnterpriseProjectItem.

        状态。 - 1：正常。 - 0：异常。

        :return: The status of this EnterpriseProjectItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnterpriseProjectItem.

        状态。 - 1：正常。 - 0：异常。

        :param status: The status of this EnterpriseProjectItem.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this EnterpriseProjectItem.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The created of this EnterpriseProjectItem.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EnterpriseProjectItem.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param created: The created of this EnterpriseProjectItem.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this EnterpriseProjectItem.

        更新时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The updated of this EnterpriseProjectItem.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this EnterpriseProjectItem.

        更新时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param updated: The updated of this EnterpriseProjectItem.
        :type updated: str
        """
        self._updated = updated

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
        if not isinstance(other, EnterpriseProjectItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
