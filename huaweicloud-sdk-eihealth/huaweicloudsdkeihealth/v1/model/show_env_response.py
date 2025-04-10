# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEnvResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dev_user_pool': 'bool',
        'has_dev': 'bool',
        'has_drug': 'bool',
        'has_encryption_button': 'bool',
        'deploy_mode': 'str',
        'enable_cold_archive': 'bool',
        'public_bucket_path': 'str'
    }

    attribute_map = {
        'dev_user_pool': 'dev_user_pool',
        'has_dev': 'has_dev',
        'has_drug': 'has_drug',
        'has_encryption_button': 'has_encryption_button',
        'deploy_mode': 'deploy_mode',
        'enable_cold_archive': 'enable_cold_archive',
        'public_bucket_path': 'public_bucket_path'
    }

    def __init__(self, dev_user_pool=None, has_dev=None, has_drug=None, has_encryption_button=None, deploy_mode=None, enable_cold_archive=None, public_bucket_path=None):
        r"""ShowEnvResponse

        The model defined in huaweicloud sdk

        :param dev_user_pool: notebook是否使用专属资源池
        :type dev_user_pool: bool
        :param has_dev: 是否集成开发环境
        :type has_dev: bool
        :param has_drug: 是否部署药物虚拟筛选
        :type has_drug: bool
        :param has_encryption_button: 是否显示加密按钮
        :type has_encryption_button: bool
        :param deploy_mode: 医疗智能体部署模式
        :type deploy_mode: str
        :param enable_cold_archive: 是否支持归档类型存储
        :type enable_cold_archive: bool
        :param public_bucket_path: 医疗智能体公共数据桶https路径
        :type public_bucket_path: str
        """
        
        super(ShowEnvResponse, self).__init__()

        self._dev_user_pool = None
        self._has_dev = None
        self._has_drug = None
        self._has_encryption_button = None
        self._deploy_mode = None
        self._enable_cold_archive = None
        self._public_bucket_path = None
        self.discriminator = None

        if dev_user_pool is not None:
            self.dev_user_pool = dev_user_pool
        if has_dev is not None:
            self.has_dev = has_dev
        if has_drug is not None:
            self.has_drug = has_drug
        if has_encryption_button is not None:
            self.has_encryption_button = has_encryption_button
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if enable_cold_archive is not None:
            self.enable_cold_archive = enable_cold_archive
        if public_bucket_path is not None:
            self.public_bucket_path = public_bucket_path

    @property
    def dev_user_pool(self):
        r"""Gets the dev_user_pool of this ShowEnvResponse.

        notebook是否使用专属资源池

        :return: The dev_user_pool of this ShowEnvResponse.
        :rtype: bool
        """
        return self._dev_user_pool

    @dev_user_pool.setter
    def dev_user_pool(self, dev_user_pool):
        r"""Sets the dev_user_pool of this ShowEnvResponse.

        notebook是否使用专属资源池

        :param dev_user_pool: The dev_user_pool of this ShowEnvResponse.
        :type dev_user_pool: bool
        """
        self._dev_user_pool = dev_user_pool

    @property
    def has_dev(self):
        r"""Gets the has_dev of this ShowEnvResponse.

        是否集成开发环境

        :return: The has_dev of this ShowEnvResponse.
        :rtype: bool
        """
        return self._has_dev

    @has_dev.setter
    def has_dev(self, has_dev):
        r"""Sets the has_dev of this ShowEnvResponse.

        是否集成开发环境

        :param has_dev: The has_dev of this ShowEnvResponse.
        :type has_dev: bool
        """
        self._has_dev = has_dev

    @property
    def has_drug(self):
        r"""Gets the has_drug of this ShowEnvResponse.

        是否部署药物虚拟筛选

        :return: The has_drug of this ShowEnvResponse.
        :rtype: bool
        """
        return self._has_drug

    @has_drug.setter
    def has_drug(self, has_drug):
        r"""Sets the has_drug of this ShowEnvResponse.

        是否部署药物虚拟筛选

        :param has_drug: The has_drug of this ShowEnvResponse.
        :type has_drug: bool
        """
        self._has_drug = has_drug

    @property
    def has_encryption_button(self):
        r"""Gets the has_encryption_button of this ShowEnvResponse.

        是否显示加密按钮

        :return: The has_encryption_button of this ShowEnvResponse.
        :rtype: bool
        """
        return self._has_encryption_button

    @has_encryption_button.setter
    def has_encryption_button(self, has_encryption_button):
        r"""Sets the has_encryption_button of this ShowEnvResponse.

        是否显示加密按钮

        :param has_encryption_button: The has_encryption_button of this ShowEnvResponse.
        :type has_encryption_button: bool
        """
        self._has_encryption_button = has_encryption_button

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this ShowEnvResponse.

        医疗智能体部署模式

        :return: The deploy_mode of this ShowEnvResponse.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this ShowEnvResponse.

        医疗智能体部署模式

        :param deploy_mode: The deploy_mode of this ShowEnvResponse.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

    @property
    def enable_cold_archive(self):
        r"""Gets the enable_cold_archive of this ShowEnvResponse.

        是否支持归档类型存储

        :return: The enable_cold_archive of this ShowEnvResponse.
        :rtype: bool
        """
        return self._enable_cold_archive

    @enable_cold_archive.setter
    def enable_cold_archive(self, enable_cold_archive):
        r"""Sets the enable_cold_archive of this ShowEnvResponse.

        是否支持归档类型存储

        :param enable_cold_archive: The enable_cold_archive of this ShowEnvResponse.
        :type enable_cold_archive: bool
        """
        self._enable_cold_archive = enable_cold_archive

    @property
    def public_bucket_path(self):
        r"""Gets the public_bucket_path of this ShowEnvResponse.

        医疗智能体公共数据桶https路径

        :return: The public_bucket_path of this ShowEnvResponse.
        :rtype: str
        """
        return self._public_bucket_path

    @public_bucket_path.setter
    def public_bucket_path(self, public_bucket_path):
        r"""Sets the public_bucket_path of this ShowEnvResponse.

        医疗智能体公共数据桶https路径

        :param public_bucket_path: The public_bucket_path of this ShowEnvResponse.
        :type public_bucket_path: str
        """
        self._public_bucket_path = public_bucket_path

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
        if not isinstance(other, ShowEnvResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
