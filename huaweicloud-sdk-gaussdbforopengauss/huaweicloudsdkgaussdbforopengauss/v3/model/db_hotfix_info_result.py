# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbHotfixInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'create_time': 'int',
        'deploy_modes': 'list[HotfixDeployMode]'
    }

    attribute_map = {
        'version': 'version',
        'create_time': 'create_time',
        'deploy_modes': 'deploy_modes'
    }

    def __init__(self, version=None, create_time=None, deploy_modes=None):
        r"""DbHotfixInfoResult

        The model defined in huaweicloud sdk

        :param version: **参数解释**： 热补丁版本。 **取值范围**： 不涉及。
        :type version: str
        :param create_time: **参数解释**： 热补丁的创建时间，UNIX时间戳格式，单位是毫秒。 **取值范围**： 不涉及。
        :type create_time: int
        :param deploy_modes: **参数解释**： 可升级该补丁的实例部署形态信息。
        :type deploy_modes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixDeployMode`]
        """
        
        

        self._version = None
        self._create_time = None
        self._deploy_modes = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if create_time is not None:
            self.create_time = create_time
        if deploy_modes is not None:
            self.deploy_modes = deploy_modes

    @property
    def version(self):
        r"""Gets the version of this DbHotfixInfoResult.

        **参数解释**： 热补丁版本。 **取值范围**： 不涉及。

        :return: The version of this DbHotfixInfoResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DbHotfixInfoResult.

        **参数解释**： 热补丁版本。 **取值范围**： 不涉及。

        :param version: The version of this DbHotfixInfoResult.
        :type version: str
        """
        self._version = version

    @property
    def create_time(self):
        r"""Gets the create_time of this DbHotfixInfoResult.

        **参数解释**： 热补丁的创建时间，UNIX时间戳格式，单位是毫秒。 **取值范围**： 不涉及。

        :return: The create_time of this DbHotfixInfoResult.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DbHotfixInfoResult.

        **参数解释**： 热补丁的创建时间，UNIX时间戳格式，单位是毫秒。 **取值范围**： 不涉及。

        :param create_time: The create_time of this DbHotfixInfoResult.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def deploy_modes(self):
        r"""Gets the deploy_modes of this DbHotfixInfoResult.

        **参数解释**： 可升级该补丁的实例部署形态信息。

        :return: The deploy_modes of this DbHotfixInfoResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixDeployMode`]
        """
        return self._deploy_modes

    @deploy_modes.setter
    def deploy_modes(self, deploy_modes):
        r"""Sets the deploy_modes of this DbHotfixInfoResult.

        **参数解释**： 可升级该补丁的实例部署形态信息。

        :param deploy_modes: The deploy_modes of this DbHotfixInfoResult.
        :type deploy_modes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixDeployMode`]
        """
        self._deploy_modes = deploy_modes

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
        if not isinstance(other, DbHotfixInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
