# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShareFeatureGatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_experience': 'bool',
        'enable_hss_service': 'bool',
        'enable_image_scan': 'bool',
        'enable_sm3': 'bool',
        'enable_image_sync': 'bool',
        'enable_cci_service': 'bool',
        'enable_image_label': 'bool',
        'enable_pipeline': 'bool',
        'enable_authorization_token': 'bool',
        'enable_resource': 'bool',
        'enable_list_v3': 'bool'
    }

    attribute_map = {
        'enable_experience': 'enable_experience',
        'enable_hss_service': 'enable_hss_service',
        'enable_image_scan': 'enable_image_scan',
        'enable_sm3': 'enable_sm3',
        'enable_image_sync': 'enable_image_sync',
        'enable_cci_service': 'enable_cci_service',
        'enable_image_label': 'enable_image_label',
        'enable_pipeline': 'enable_pipeline',
        'enable_authorization_token': 'enable_authorization_token',
        'enable_resource': 'enable_resource',
        'enable_list_v3': 'enable_list_v3'
    }

    def __init__(self, enable_experience=None, enable_hss_service=None, enable_image_scan=None, enable_sm3=None, enable_image_sync=None, enable_cci_service=None, enable_image_label=None, enable_pipeline=None, enable_authorization_token=None, enable_resource=None, enable_list_v3=None):
        r"""ShowShareFeatureGatesResponse

        The model defined in huaweicloud sdk

        :param enable_experience: 是否支持体验馆
        :type enable_experience: bool
        :param enable_hss_service: 是否支持对接hss服务
        :type enable_hss_service: bool
        :param enable_image_scan: 是否支持镜像扫描
        :type enable_image_scan: bool
        :param enable_sm3: 是否支持国密场景
        :type enable_sm3: bool
        :param enable_image_sync: 是否支持镜像同步
        :type enable_image_sync: bool
        :param enable_cci_service: 是否支持对接cci服务
        :type enable_cci_service: bool
        :param enable_image_label: 是否支持镜像标签
        :type enable_image_label: bool
        :param enable_pipeline: 是否支持流水线服务
        :type enable_pipeline: bool
        :param enable_authorization_token: 是否支持增强型临时登录指令。设置为true时，前端获取登录指令时可以选择获取增强型登录指令。
        :type enable_authorization_token: bool
        :param enable_resource: 是否支持镜像资源。设置为true时，前端界面显示“镜像资源”页签，可查看镜像中心。
        :type enable_resource: bool
        :param enable_list_v3: 是否支持list v3接口
        :type enable_list_v3: bool
        """
        
        super(ShowShareFeatureGatesResponse, self).__init__()

        self._enable_experience = None
        self._enable_hss_service = None
        self._enable_image_scan = None
        self._enable_sm3 = None
        self._enable_image_sync = None
        self._enable_cci_service = None
        self._enable_image_label = None
        self._enable_pipeline = None
        self._enable_authorization_token = None
        self._enable_resource = None
        self._enable_list_v3 = None
        self.discriminator = None

        if enable_experience is not None:
            self.enable_experience = enable_experience
        if enable_hss_service is not None:
            self.enable_hss_service = enable_hss_service
        if enable_image_scan is not None:
            self.enable_image_scan = enable_image_scan
        if enable_sm3 is not None:
            self.enable_sm3 = enable_sm3
        if enable_image_sync is not None:
            self.enable_image_sync = enable_image_sync
        if enable_cci_service is not None:
            self.enable_cci_service = enable_cci_service
        if enable_image_label is not None:
            self.enable_image_label = enable_image_label
        if enable_pipeline is not None:
            self.enable_pipeline = enable_pipeline
        if enable_authorization_token is not None:
            self.enable_authorization_token = enable_authorization_token
        if enable_resource is not None:
            self.enable_resource = enable_resource
        if enable_list_v3 is not None:
            self.enable_list_v3 = enable_list_v3

    @property
    def enable_experience(self):
        r"""Gets the enable_experience of this ShowShareFeatureGatesResponse.

        是否支持体验馆

        :return: The enable_experience of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_experience

    @enable_experience.setter
    def enable_experience(self, enable_experience):
        r"""Sets the enable_experience of this ShowShareFeatureGatesResponse.

        是否支持体验馆

        :param enable_experience: The enable_experience of this ShowShareFeatureGatesResponse.
        :type enable_experience: bool
        """
        self._enable_experience = enable_experience

    @property
    def enable_hss_service(self):
        r"""Gets the enable_hss_service of this ShowShareFeatureGatesResponse.

        是否支持对接hss服务

        :return: The enable_hss_service of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_hss_service

    @enable_hss_service.setter
    def enable_hss_service(self, enable_hss_service):
        r"""Sets the enable_hss_service of this ShowShareFeatureGatesResponse.

        是否支持对接hss服务

        :param enable_hss_service: The enable_hss_service of this ShowShareFeatureGatesResponse.
        :type enable_hss_service: bool
        """
        self._enable_hss_service = enable_hss_service

    @property
    def enable_image_scan(self):
        r"""Gets the enable_image_scan of this ShowShareFeatureGatesResponse.

        是否支持镜像扫描

        :return: The enable_image_scan of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_image_scan

    @enable_image_scan.setter
    def enable_image_scan(self, enable_image_scan):
        r"""Sets the enable_image_scan of this ShowShareFeatureGatesResponse.

        是否支持镜像扫描

        :param enable_image_scan: The enable_image_scan of this ShowShareFeatureGatesResponse.
        :type enable_image_scan: bool
        """
        self._enable_image_scan = enable_image_scan

    @property
    def enable_sm3(self):
        r"""Gets the enable_sm3 of this ShowShareFeatureGatesResponse.

        是否支持国密场景

        :return: The enable_sm3 of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_sm3

    @enable_sm3.setter
    def enable_sm3(self, enable_sm3):
        r"""Sets the enable_sm3 of this ShowShareFeatureGatesResponse.

        是否支持国密场景

        :param enable_sm3: The enable_sm3 of this ShowShareFeatureGatesResponse.
        :type enable_sm3: bool
        """
        self._enable_sm3 = enable_sm3

    @property
    def enable_image_sync(self):
        r"""Gets the enable_image_sync of this ShowShareFeatureGatesResponse.

        是否支持镜像同步

        :return: The enable_image_sync of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_image_sync

    @enable_image_sync.setter
    def enable_image_sync(self, enable_image_sync):
        r"""Sets the enable_image_sync of this ShowShareFeatureGatesResponse.

        是否支持镜像同步

        :param enable_image_sync: The enable_image_sync of this ShowShareFeatureGatesResponse.
        :type enable_image_sync: bool
        """
        self._enable_image_sync = enable_image_sync

    @property
    def enable_cci_service(self):
        r"""Gets the enable_cci_service of this ShowShareFeatureGatesResponse.

        是否支持对接cci服务

        :return: The enable_cci_service of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_cci_service

    @enable_cci_service.setter
    def enable_cci_service(self, enable_cci_service):
        r"""Sets the enable_cci_service of this ShowShareFeatureGatesResponse.

        是否支持对接cci服务

        :param enable_cci_service: The enable_cci_service of this ShowShareFeatureGatesResponse.
        :type enable_cci_service: bool
        """
        self._enable_cci_service = enable_cci_service

    @property
    def enable_image_label(self):
        r"""Gets the enable_image_label of this ShowShareFeatureGatesResponse.

        是否支持镜像标签

        :return: The enable_image_label of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_image_label

    @enable_image_label.setter
    def enable_image_label(self, enable_image_label):
        r"""Sets the enable_image_label of this ShowShareFeatureGatesResponse.

        是否支持镜像标签

        :param enable_image_label: The enable_image_label of this ShowShareFeatureGatesResponse.
        :type enable_image_label: bool
        """
        self._enable_image_label = enable_image_label

    @property
    def enable_pipeline(self):
        r"""Gets the enable_pipeline of this ShowShareFeatureGatesResponse.

        是否支持流水线服务

        :return: The enable_pipeline of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_pipeline

    @enable_pipeline.setter
    def enable_pipeline(self, enable_pipeline):
        r"""Sets the enable_pipeline of this ShowShareFeatureGatesResponse.

        是否支持流水线服务

        :param enable_pipeline: The enable_pipeline of this ShowShareFeatureGatesResponse.
        :type enable_pipeline: bool
        """
        self._enable_pipeline = enable_pipeline

    @property
    def enable_authorization_token(self):
        r"""Gets the enable_authorization_token of this ShowShareFeatureGatesResponse.

        是否支持增强型临时登录指令。设置为true时，前端获取登录指令时可以选择获取增强型登录指令。

        :return: The enable_authorization_token of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_authorization_token

    @enable_authorization_token.setter
    def enable_authorization_token(self, enable_authorization_token):
        r"""Sets the enable_authorization_token of this ShowShareFeatureGatesResponse.

        是否支持增强型临时登录指令。设置为true时，前端获取登录指令时可以选择获取增强型登录指令。

        :param enable_authorization_token: The enable_authorization_token of this ShowShareFeatureGatesResponse.
        :type enable_authorization_token: bool
        """
        self._enable_authorization_token = enable_authorization_token

    @property
    def enable_resource(self):
        r"""Gets the enable_resource of this ShowShareFeatureGatesResponse.

        是否支持镜像资源。设置为true时，前端界面显示“镜像资源”页签，可查看镜像中心。

        :return: The enable_resource of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_resource

    @enable_resource.setter
    def enable_resource(self, enable_resource):
        r"""Sets the enable_resource of this ShowShareFeatureGatesResponse.

        是否支持镜像资源。设置为true时，前端界面显示“镜像资源”页签，可查看镜像中心。

        :param enable_resource: The enable_resource of this ShowShareFeatureGatesResponse.
        :type enable_resource: bool
        """
        self._enable_resource = enable_resource

    @property
    def enable_list_v3(self):
        r"""Gets the enable_list_v3 of this ShowShareFeatureGatesResponse.

        是否支持list v3接口

        :return: The enable_list_v3 of this ShowShareFeatureGatesResponse.
        :rtype: bool
        """
        return self._enable_list_v3

    @enable_list_v3.setter
    def enable_list_v3(self, enable_list_v3):
        r"""Sets the enable_list_v3 of this ShowShareFeatureGatesResponse.

        是否支持list v3接口

        :param enable_list_v3: The enable_list_v3 of this ShowShareFeatureGatesResponse.
        :type enable_list_v3: bool
        """
        self._enable_list_v3 = enable_list_v3

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
        if not isinstance(other, ShowShareFeatureGatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
