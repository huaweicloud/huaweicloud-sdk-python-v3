# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppNodeModel:

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
        'gmt_create': 'date',
        'gmt_modify': 'date',
        'name': 'str',
        'business_id': 'int',
        'sub_business_id': 'int',
        'inner_domain_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'gmt_create': 'gmt_create',
        'gmt_modify': 'gmt_modify',
        'name': 'name',
        'business_id': 'business_id',
        'sub_business_id': 'sub_business_id',
        'inner_domain_id': 'inner_domain_id'
    }

    def __init__(self, id=None, gmt_create=None, gmt_modify=None, name=None, business_id=None, sub_business_id=None, inner_domain_id=None):
        """AppNodeModel

        The model defined in huaweicloud sdk

        :param id: 组件id。
        :type id: int
        :param gmt_create: 创建时间。
        :type gmt_create: date
        :param gmt_modify: 修改时间。
        :type gmt_modify: date
        :param name: 组件名称。
        :type name: str
        :param business_id: 应用id。
        :type business_id: int
        :param sub_business_id: 子应用id。
        :type sub_business_id: int
        :param inner_domain_id: 租户id。
        :type inner_domain_id: int
        """
        
        

        self._id = None
        self._gmt_create = None
        self._gmt_modify = None
        self._name = None
        self._business_id = None
        self._sub_business_id = None
        self._inner_domain_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if gmt_create is not None:
            self.gmt_create = gmt_create
        if gmt_modify is not None:
            self.gmt_modify = gmt_modify
        if name is not None:
            self.name = name
        if business_id is not None:
            self.business_id = business_id
        if sub_business_id is not None:
            self.sub_business_id = sub_business_id
        if inner_domain_id is not None:
            self.inner_domain_id = inner_domain_id

    @property
    def id(self):
        """Gets the id of this AppNodeModel.

        组件id。

        :return: The id of this AppNodeModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppNodeModel.

        组件id。

        :param id: The id of this AppNodeModel.
        :type id: int
        """
        self._id = id

    @property
    def gmt_create(self):
        """Gets the gmt_create of this AppNodeModel.

        创建时间。

        :return: The gmt_create of this AppNodeModel.
        :rtype: date
        """
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, gmt_create):
        """Sets the gmt_create of this AppNodeModel.

        创建时间。

        :param gmt_create: The gmt_create of this AppNodeModel.
        :type gmt_create: date
        """
        self._gmt_create = gmt_create

    @property
    def gmt_modify(self):
        """Gets the gmt_modify of this AppNodeModel.

        修改时间。

        :return: The gmt_modify of this AppNodeModel.
        :rtype: date
        """
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, gmt_modify):
        """Sets the gmt_modify of this AppNodeModel.

        修改时间。

        :param gmt_modify: The gmt_modify of this AppNodeModel.
        :type gmt_modify: date
        """
        self._gmt_modify = gmt_modify

    @property
    def name(self):
        """Gets the name of this AppNodeModel.

        组件名称。

        :return: The name of this AppNodeModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppNodeModel.

        组件名称。

        :param name: The name of this AppNodeModel.
        :type name: str
        """
        self._name = name

    @property
    def business_id(self):
        """Gets the business_id of this AppNodeModel.

        应用id。

        :return: The business_id of this AppNodeModel.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this AppNodeModel.

        应用id。

        :param business_id: The business_id of this AppNodeModel.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def sub_business_id(self):
        """Gets the sub_business_id of this AppNodeModel.

        子应用id。

        :return: The sub_business_id of this AppNodeModel.
        :rtype: int
        """
        return self._sub_business_id

    @sub_business_id.setter
    def sub_business_id(self, sub_business_id):
        """Sets the sub_business_id of this AppNodeModel.

        子应用id。

        :param sub_business_id: The sub_business_id of this AppNodeModel.
        :type sub_business_id: int
        """
        self._sub_business_id = sub_business_id

    @property
    def inner_domain_id(self):
        """Gets the inner_domain_id of this AppNodeModel.

        租户id。

        :return: The inner_domain_id of this AppNodeModel.
        :rtype: int
        """
        return self._inner_domain_id

    @inner_domain_id.setter
    def inner_domain_id(self, inner_domain_id):
        """Sets the inner_domain_id of this AppNodeModel.

        租户id。

        :param inner_domain_id: The inner_domain_id of this AppNodeModel.
        :type inner_domain_id: int
        """
        self._inner_domain_id = inner_domain_id

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
        if not isinstance(other, AppNodeModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
