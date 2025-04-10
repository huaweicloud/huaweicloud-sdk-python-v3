# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceEngineDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_version': 'str',
        'instances': 'list[InstanceDetail]'
    }

    attribute_map = {
        'engine_version': 'engine_version',
        'instances': 'instances'
    }

    def __init__(self, engine_version=None, instances=None):
        r"""InstanceEngineDetail

        The model defined in huaweicloud sdk

        :param engine_version: 引擎版本号。
        :type engine_version: str
        :param instances: 实例详情。
        :type instances: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceDetail`]
        """
        
        

        self._engine_version = None
        self._instances = None
        self.discriminator = None

        if engine_version is not None:
            self.engine_version = engine_version
        if instances is not None:
            self.instances = instances

    @property
    def engine_version(self):
        r"""Gets the engine_version of this InstanceEngineDetail.

        引擎版本号。

        :return: The engine_version of this InstanceEngineDetail.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this InstanceEngineDetail.

        引擎版本号。

        :param engine_version: The engine_version of this InstanceEngineDetail.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def instances(self):
        r"""Gets the instances of this InstanceEngineDetail.

        实例详情。

        :return: The instances of this InstanceEngineDetail.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceDetail`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this InstanceEngineDetail.

        实例详情。

        :param instances: The instances of this InstanceEngineDetail.
        :type instances: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceDetail`]
        """
        self._instances = instances

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
        if not isinstance(other, InstanceEngineDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
