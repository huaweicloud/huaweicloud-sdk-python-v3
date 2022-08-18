# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDependenciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'maxitems': 'str',
        'ispublic': 'str',
        'dependency_type': 'str',
        'runtime': 'str',
        'name': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'maxitems': 'maxitems',
        'ispublic': 'ispublic',
        'dependency_type': 'dependency_type',
        'runtime': 'runtime',
        'name': 'name',
        'limit': 'limit'
    }

    def __init__(self, marker=None, maxitems=None, ispublic=None, dependency_type=None, runtime=None, name=None, limit=None):
        """ListDependenciesRequest

        The model defined in huaweicloud sdk

        :param marker: 上一次查询依赖包的最后记录位置，默认为\&quot;0\&quot;。
        :type marker: str
        :param maxitems: 单次查询最大条数
        :type maxitems: str
        :param ispublic: 是否为公共依赖包
        :type ispublic: str
        :param dependency_type: 依赖包类型public：公开,private:私有，all：全部。缺省时查询全量
        :type dependency_type: str
        :param runtime: FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本
        :type runtime: str
        :param name: 依赖包名称。
        :type name: str
        :param limit: 本次查询可获取的依赖包的最大数目，默认为\&quot;400\&quot;。
        :type limit: str
        """
        
        

        self._marker = None
        self._maxitems = None
        self._ispublic = None
        self._dependency_type = None
        self._runtime = None
        self._name = None
        self._limit = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if maxitems is not None:
            self.maxitems = maxitems
        if ispublic is not None:
            self.ispublic = ispublic
        if dependency_type is not None:
            self.dependency_type = dependency_type
        if runtime is not None:
            self.runtime = runtime
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListDependenciesRequest.

        上一次查询依赖包的最后记录位置，默认为\"0\"。

        :return: The marker of this ListDependenciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDependenciesRequest.

        上一次查询依赖包的最后记录位置，默认为\"0\"。

        :param marker: The marker of this ListDependenciesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def maxitems(self):
        """Gets the maxitems of this ListDependenciesRequest.

        单次查询最大条数

        :return: The maxitems of this ListDependenciesRequest.
        :rtype: str
        """
        return self._maxitems

    @maxitems.setter
    def maxitems(self, maxitems):
        """Sets the maxitems of this ListDependenciesRequest.

        单次查询最大条数

        :param maxitems: The maxitems of this ListDependenciesRequest.
        :type maxitems: str
        """
        self._maxitems = maxitems

    @property
    def ispublic(self):
        """Gets the ispublic of this ListDependenciesRequest.

        是否为公共依赖包

        :return: The ispublic of this ListDependenciesRequest.
        :rtype: str
        """
        return self._ispublic

    @ispublic.setter
    def ispublic(self, ispublic):
        """Sets the ispublic of this ListDependenciesRequest.

        是否为公共依赖包

        :param ispublic: The ispublic of this ListDependenciesRequest.
        :type ispublic: str
        """
        self._ispublic = ispublic

    @property
    def dependency_type(self):
        """Gets the dependency_type of this ListDependenciesRequest.

        依赖包类型public：公开,private:私有，all：全部。缺省时查询全量

        :return: The dependency_type of this ListDependenciesRequest.
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this ListDependenciesRequest.

        依赖包类型public：公开,private:私有，all：全部。缺省时查询全量

        :param dependency_type: The dependency_type of this ListDependenciesRequest.
        :type dependency_type: str
        """
        self._dependency_type = dependency_type

    @property
    def runtime(self):
        """Gets the runtime of this ListDependenciesRequest.

        FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本

        :return: The runtime of this ListDependenciesRequest.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ListDependenciesRequest.

        FunctionGraph函数的执行环境 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Python3.9: Python语言3.9版本。 Go1.8: Go语言1.8版本。 Go1.x: Go语言1.x版本。 Java8: Java语言8版本。 Java11: Java语言11版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 Node.js10.16: Nodejs语言10.16版本。 Node.js12.13: Nodejs语言12.13版本。 Node.js14.18: Nodejs语言14.18版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本

        :param runtime: The runtime of this ListDependenciesRequest.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def name(self):
        """Gets the name of this ListDependenciesRequest.

        依赖包名称。

        :return: The name of this ListDependenciesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDependenciesRequest.

        依赖包名称。

        :param name: The name of this ListDependenciesRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListDependenciesRequest.

        本次查询可获取的依赖包的最大数目，默认为\"400\"。

        :return: The limit of this ListDependenciesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDependenciesRequest.

        本次查询可获取的依赖包的最大数目，默认为\"400\"。

        :param limit: The limit of this ListDependenciesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListDependenciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
