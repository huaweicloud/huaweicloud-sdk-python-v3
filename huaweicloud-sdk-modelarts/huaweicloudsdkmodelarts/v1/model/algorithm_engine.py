# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_id': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'v1_compatible': 'bool',
        'run_user': 'str',
        'image_url': 'str'
    }

    attribute_map = {
        'engine_id': 'engine_id',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'v1_compatible': 'v1_compatible',
        'run_user': 'run_user',
        'image_url': 'image_url'
    }

    def __init__(self, engine_id=None, engine_name=None, engine_version=None, v1_compatible=None, run_user=None, image_url=None):
        r"""AlgorithmEngine

        The model defined in huaweicloud sdk

        :param engine_id: 引擎规格的ID。如“caffe-1.0.0-python2.7”。
        :type engine_id: str
        :param engine_name: 引擎规格的名称。如“Caffe”。
        :type engine_name: str
        :param engine_version: 引擎规格的版本。对一个引擎名称，有多个版本的引擎，如使用python2.7的\&quot;Caffe-1.0.0-python2.7\&quot;等。
        :type engine_version: str
        :param v1_compatible: 是否为v1兼容模式。
        :type v1_compatible: bool
        :param run_user: 引擎默认启动用户uid。
        :type run_user: str
        :param image_url: 算法选择的自定义镜像地址。
        :type image_url: str
        """
        
        

        self._engine_id = None
        self._engine_name = None
        self._engine_version = None
        self._v1_compatible = None
        self._run_user = None
        self._image_url = None
        self.discriminator = None

        if engine_id is not None:
            self.engine_id = engine_id
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if v1_compatible is not None:
            self.v1_compatible = v1_compatible
        if run_user is not None:
            self.run_user = run_user
        if image_url is not None:
            self.image_url = image_url

    @property
    def engine_id(self):
        r"""Gets the engine_id of this AlgorithmEngine.

        引擎规格的ID。如“caffe-1.0.0-python2.7”。

        :return: The engine_id of this AlgorithmEngine.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this AlgorithmEngine.

        引擎规格的ID。如“caffe-1.0.0-python2.7”。

        :param engine_id: The engine_id of this AlgorithmEngine.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def engine_name(self):
        r"""Gets the engine_name of this AlgorithmEngine.

        引擎规格的名称。如“Caffe”。

        :return: The engine_name of this AlgorithmEngine.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this AlgorithmEngine.

        引擎规格的名称。如“Caffe”。

        :param engine_name: The engine_name of this AlgorithmEngine.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this AlgorithmEngine.

        引擎规格的版本。对一个引擎名称，有多个版本的引擎，如使用python2.7的\"Caffe-1.0.0-python2.7\"等。

        :return: The engine_version of this AlgorithmEngine.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this AlgorithmEngine.

        引擎规格的版本。对一个引擎名称，有多个版本的引擎，如使用python2.7的\"Caffe-1.0.0-python2.7\"等。

        :param engine_version: The engine_version of this AlgorithmEngine.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def v1_compatible(self):
        r"""Gets the v1_compatible of this AlgorithmEngine.

        是否为v1兼容模式。

        :return: The v1_compatible of this AlgorithmEngine.
        :rtype: bool
        """
        return self._v1_compatible

    @v1_compatible.setter
    def v1_compatible(self, v1_compatible):
        r"""Sets the v1_compatible of this AlgorithmEngine.

        是否为v1兼容模式。

        :param v1_compatible: The v1_compatible of this AlgorithmEngine.
        :type v1_compatible: bool
        """
        self._v1_compatible = v1_compatible

    @property
    def run_user(self):
        r"""Gets the run_user of this AlgorithmEngine.

        引擎默认启动用户uid。

        :return: The run_user of this AlgorithmEngine.
        :rtype: str
        """
        return self._run_user

    @run_user.setter
    def run_user(self, run_user):
        r"""Sets the run_user of this AlgorithmEngine.

        引擎默认启动用户uid。

        :param run_user: The run_user of this AlgorithmEngine.
        :type run_user: str
        """
        self._run_user = run_user

    @property
    def image_url(self):
        r"""Gets the image_url of this AlgorithmEngine.

        算法选择的自定义镜像地址。

        :return: The image_url of this AlgorithmEngine.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this AlgorithmEngine.

        算法选择的自定义镜像地址。

        :param image_url: The image_url of this AlgorithmEngine.
        :type image_url: str
        """
        self._image_url = image_url

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlgorithmEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
