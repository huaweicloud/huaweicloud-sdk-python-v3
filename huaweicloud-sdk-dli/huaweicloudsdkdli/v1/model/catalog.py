# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Catalog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'create_time': 'int',
        'parameters': 'dict(str, str)',
        'description': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'create_time': 'create_time',
        'parameters': 'parameters',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, name=None, create_time=None, parameters=None, description=None, status=None):
        r"""Catalog

        The model defined in huaweicloud sdk

        :param name: DLI侧catalog映射名称。
        :type name: str
        :param create_time: 创建时间
        :type create_time: int
        :param parameters: 属性中包含type和externalCatalog
        :type parameters: dict(str, str)
        :param description: 描述
        :type description: str
        :param status: catalog状态。CREATING：catalog创建中；ACTIVE：catalog可使用；FAILED：catalog创建失败。
        :type status: str
        """
        
        

        self._name = None
        self._create_time = None
        self._parameters = None
        self._description = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if parameters is not None:
            self.parameters = parameters
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this Catalog.

        DLI侧catalog映射名称。

        :return: The name of this Catalog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Catalog.

        DLI侧catalog映射名称。

        :param name: The name of this Catalog.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        r"""Gets the create_time of this Catalog.

        创建时间

        :return: The create_time of this Catalog.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Catalog.

        创建时间

        :param create_time: The create_time of this Catalog.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def parameters(self):
        r"""Gets the parameters of this Catalog.

        属性中包含type和externalCatalog

        :return: The parameters of this Catalog.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this Catalog.

        属性中包含type和externalCatalog

        :param parameters: The parameters of this Catalog.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def description(self):
        r"""Gets the description of this Catalog.

        描述

        :return: The description of this Catalog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Catalog.

        描述

        :param description: The description of this Catalog.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this Catalog.

        catalog状态。CREATING：catalog创建中；ACTIVE：catalog可使用；FAILED：catalog创建失败。

        :return: The status of this Catalog.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Catalog.

        catalog状态。CREATING：catalog创建中；ACTIVE：catalog可使用；FAILED：catalog创建失败。

        :param status: The status of this Catalog.
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
        if not isinstance(other, Catalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
