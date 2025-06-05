# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_name': 'str',
        'runtime_path': 'str'
    }

    attribute_map = {
        'runtime_name': 'runtime_name',
        'runtime_path': 'runtime_path'
    }

    def __init__(self, runtime_name=None, runtime_path=None):
        r"""RuntimeRequestBody

        The model defined in huaweicloud sdk

        :param runtime_name: 运行时名称：   - crio_endpoint：CRIO   - containerd_endpoint：Containerd   - docker_endpoint：Docker   - isulad_endpoint：Isulad   - podman_endpoint：Podman 
        :type runtime_name: str
        :param runtime_path: 运行时路径
        :type runtime_path: str
        """
        
        

        self._runtime_name = None
        self._runtime_path = None
        self.discriminator = None

        if runtime_name is not None:
            self.runtime_name = runtime_name
        if runtime_path is not None:
            self.runtime_path = runtime_path

    @property
    def runtime_name(self):
        r"""Gets the runtime_name of this RuntimeRequestBody.

        运行时名称：   - crio_endpoint：CRIO   - containerd_endpoint：Containerd   - docker_endpoint：Docker   - isulad_endpoint：Isulad   - podman_endpoint：Podman 

        :return: The runtime_name of this RuntimeRequestBody.
        :rtype: str
        """
        return self._runtime_name

    @runtime_name.setter
    def runtime_name(self, runtime_name):
        r"""Sets the runtime_name of this RuntimeRequestBody.

        运行时名称：   - crio_endpoint：CRIO   - containerd_endpoint：Containerd   - docker_endpoint：Docker   - isulad_endpoint：Isulad   - podman_endpoint：Podman 

        :param runtime_name: The runtime_name of this RuntimeRequestBody.
        :type runtime_name: str
        """
        self._runtime_name = runtime_name

    @property
    def runtime_path(self):
        r"""Gets the runtime_path of this RuntimeRequestBody.

        运行时路径

        :return: The runtime_path of this RuntimeRequestBody.
        :rtype: str
        """
        return self._runtime_path

    @runtime_path.setter
    def runtime_path(self, runtime_path):
        r"""Sets the runtime_path of this RuntimeRequestBody.

        运行时路径

        :param runtime_path: The runtime_path of this RuntimeRequestBody.
        :type runtime_path: str
        """
        self._runtime_path = runtime_path

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
        if not isinstance(other, RuntimeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
