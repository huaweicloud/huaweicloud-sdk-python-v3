# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_bridge': 'bool',
        'enable_profile': 'bool',
        'enable_classification': 'bool',
        'bridge_status': 'str',
        'profile_status': 'str',
        'classification_status': 'str',
        'bridge_job_log': 'str',
        'profile_job_log': 'str',
        'classification_job_log': 'str'
    }

    attribute_map = {
        'enable_bridge': 'enable_bridge',
        'enable_profile': 'enable_profile',
        'enable_classification': 'enable_classification',
        'bridge_status': 'bridge_status',
        'profile_status': 'profile_status',
        'classification_status': 'classification_status',
        'bridge_job_log': 'bridge_job_log',
        'profile_job_log': 'profile_job_log',
        'classification_job_log': 'classification_job_log'
    }

    def __init__(self, enable_bridge=None, enable_profile=None, enable_classification=None, bridge_status=None, profile_status=None, classification_status=None, bridge_job_log=None, profile_job_log=None, classification_job_log=None):
        """ShowInstanceLogResponse

        The model defined in huaweicloud sdk

        :param enable_bridge: 是否开启桥接模式
        :type enable_bridge: bool
        :param enable_profile: 是否启用配置
        :type enable_profile: bool
        :param enable_classification: 是否开启分类
        :type enable_classification: bool
        :param bridge_status: 桥接状态
        :type bridge_status: str
        :param profile_status: 配置状态
        :type profile_status: str
        :param classification_status: 分类状态
        :type classification_status: str
        :param bridge_job_log: 桥接作业日志
        :type bridge_job_log: str
        :param profile_job_log: 配置作业日志
        :type profile_job_log: str
        :param classification_job_log: 分类作业日志
        :type classification_job_log: str
        """
        
        super(ShowInstanceLogResponse, self).__init__()

        self._enable_bridge = None
        self._enable_profile = None
        self._enable_classification = None
        self._bridge_status = None
        self._profile_status = None
        self._classification_status = None
        self._bridge_job_log = None
        self._profile_job_log = None
        self._classification_job_log = None
        self.discriminator = None

        if enable_bridge is not None:
            self.enable_bridge = enable_bridge
        if enable_profile is not None:
            self.enable_profile = enable_profile
        if enable_classification is not None:
            self.enable_classification = enable_classification
        if bridge_status is not None:
            self.bridge_status = bridge_status
        if profile_status is not None:
            self.profile_status = profile_status
        if classification_status is not None:
            self.classification_status = classification_status
        if bridge_job_log is not None:
            self.bridge_job_log = bridge_job_log
        if profile_job_log is not None:
            self.profile_job_log = profile_job_log
        if classification_job_log is not None:
            self.classification_job_log = classification_job_log

    @property
    def enable_bridge(self):
        """Gets the enable_bridge of this ShowInstanceLogResponse.

        是否开启桥接模式

        :return: The enable_bridge of this ShowInstanceLogResponse.
        :rtype: bool
        """
        return self._enable_bridge

    @enable_bridge.setter
    def enable_bridge(self, enable_bridge):
        """Sets the enable_bridge of this ShowInstanceLogResponse.

        是否开启桥接模式

        :param enable_bridge: The enable_bridge of this ShowInstanceLogResponse.
        :type enable_bridge: bool
        """
        self._enable_bridge = enable_bridge

    @property
    def enable_profile(self):
        """Gets the enable_profile of this ShowInstanceLogResponse.

        是否启用配置

        :return: The enable_profile of this ShowInstanceLogResponse.
        :rtype: bool
        """
        return self._enable_profile

    @enable_profile.setter
    def enable_profile(self, enable_profile):
        """Sets the enable_profile of this ShowInstanceLogResponse.

        是否启用配置

        :param enable_profile: The enable_profile of this ShowInstanceLogResponse.
        :type enable_profile: bool
        """
        self._enable_profile = enable_profile

    @property
    def enable_classification(self):
        """Gets the enable_classification of this ShowInstanceLogResponse.

        是否开启分类

        :return: The enable_classification of this ShowInstanceLogResponse.
        :rtype: bool
        """
        return self._enable_classification

    @enable_classification.setter
    def enable_classification(self, enable_classification):
        """Sets the enable_classification of this ShowInstanceLogResponse.

        是否开启分类

        :param enable_classification: The enable_classification of this ShowInstanceLogResponse.
        :type enable_classification: bool
        """
        self._enable_classification = enable_classification

    @property
    def bridge_status(self):
        """Gets the bridge_status of this ShowInstanceLogResponse.

        桥接状态

        :return: The bridge_status of this ShowInstanceLogResponse.
        :rtype: str
        """
        return self._bridge_status

    @bridge_status.setter
    def bridge_status(self, bridge_status):
        """Sets the bridge_status of this ShowInstanceLogResponse.

        桥接状态

        :param bridge_status: The bridge_status of this ShowInstanceLogResponse.
        :type bridge_status: str
        """
        self._bridge_status = bridge_status

    @property
    def profile_status(self):
        """Gets the profile_status of this ShowInstanceLogResponse.

        配置状态

        :return: The profile_status of this ShowInstanceLogResponse.
        :rtype: str
        """
        return self._profile_status

    @profile_status.setter
    def profile_status(self, profile_status):
        """Sets the profile_status of this ShowInstanceLogResponse.

        配置状态

        :param profile_status: The profile_status of this ShowInstanceLogResponse.
        :type profile_status: str
        """
        self._profile_status = profile_status

    @property
    def classification_status(self):
        """Gets the classification_status of this ShowInstanceLogResponse.

        分类状态

        :return: The classification_status of this ShowInstanceLogResponse.
        :rtype: str
        """
        return self._classification_status

    @classification_status.setter
    def classification_status(self, classification_status):
        """Sets the classification_status of this ShowInstanceLogResponse.

        分类状态

        :param classification_status: The classification_status of this ShowInstanceLogResponse.
        :type classification_status: str
        """
        self._classification_status = classification_status

    @property
    def bridge_job_log(self):
        """Gets the bridge_job_log of this ShowInstanceLogResponse.

        桥接作业日志

        :return: The bridge_job_log of this ShowInstanceLogResponse.
        :rtype: str
        """
        return self._bridge_job_log

    @bridge_job_log.setter
    def bridge_job_log(self, bridge_job_log):
        """Sets the bridge_job_log of this ShowInstanceLogResponse.

        桥接作业日志

        :param bridge_job_log: The bridge_job_log of this ShowInstanceLogResponse.
        :type bridge_job_log: str
        """
        self._bridge_job_log = bridge_job_log

    @property
    def profile_job_log(self):
        """Gets the profile_job_log of this ShowInstanceLogResponse.

        配置作业日志

        :return: The profile_job_log of this ShowInstanceLogResponse.
        :rtype: str
        """
        return self._profile_job_log

    @profile_job_log.setter
    def profile_job_log(self, profile_job_log):
        """Sets the profile_job_log of this ShowInstanceLogResponse.

        配置作业日志

        :param profile_job_log: The profile_job_log of this ShowInstanceLogResponse.
        :type profile_job_log: str
        """
        self._profile_job_log = profile_job_log

    @property
    def classification_job_log(self):
        """Gets the classification_job_log of this ShowInstanceLogResponse.

        分类作业日志

        :return: The classification_job_log of this ShowInstanceLogResponse.
        :rtype: str
        """
        return self._classification_job_log

    @classification_job_log.setter
    def classification_job_log(self, classification_job_log):
        """Sets the classification_job_log of this ShowInstanceLogResponse.

        分类作业日志

        :param classification_job_log: The classification_job_log of this ShowInstanceLogResponse.
        :type classification_job_log: str
        """
        self._classification_job_log = classification_job_log

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
        if not isinstance(other, ShowInstanceLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
