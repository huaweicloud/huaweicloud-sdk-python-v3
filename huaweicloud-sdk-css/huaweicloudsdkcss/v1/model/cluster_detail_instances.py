# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDetailInstances:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'spec_code': 'str',
        'az_code': 'str'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'spec_code': 'specCode',
        'az_code': 'azCode'
    }

    def __init__(self, status=None, type=None, id=None, name=None, spec_code=None, az_code=None):
        """ClusterDetailInstances - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._type = None
        self._id = None
        self._name = None
        self._spec_code = None
        self._az_code = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if spec_code is not None:
            self.spec_code = spec_code
        if az_code is not None:
            self.az_code = az_code

    @property
    def status(self):
        """Gets the status of this ClusterDetailInstances.

        状态。  - 100：操作进行中，如创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :return: The status of this ClusterDetailInstances.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterDetailInstances.

        状态。  - 100：操作进行中，如创建中。 - 200：可用。 - 303：不可用，如创建失败。

        :param status: The status of this ClusterDetailInstances.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ClusterDetailInstances.

        支持类型：ess（Elasticsearch节点）。

        :return: The type of this ClusterDetailInstances.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterDetailInstances.

        支持类型：ess（Elasticsearch节点）。

        :param type: The type of this ClusterDetailInstances.
        :type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this ClusterDetailInstances.

        实例ID。

        :return: The id of this ClusterDetailInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterDetailInstances.

        实例ID。

        :param id: The id of this ClusterDetailInstances.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterDetailInstances.

        实例名字。

        :return: The name of this ClusterDetailInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterDetailInstances.

        实例名字。

        :param name: The name of this ClusterDetailInstances.
        :type: str
        """
        self._name = name

    @property
    def spec_code(self):
        """Gets the spec_code of this ClusterDetailInstances.

        节点规格名称。

        :return: The spec_code of this ClusterDetailInstances.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ClusterDetailInstances.

        节点规格名称。

        :param spec_code: The spec_code of this ClusterDetailInstances.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def az_code(self):
        """Gets the az_code of this ClusterDetailInstances.

        节点所属AZ信息。

        :return: The az_code of this ClusterDetailInstances.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this ClusterDetailInstances.

        节点所属AZ信息。

        :param az_code: The az_code of this ClusterDetailInstances.
        :type: str
        """
        self._az_code = az_code

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
        if not isinstance(other, ClusterDetailInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
