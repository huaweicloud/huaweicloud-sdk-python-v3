# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service': 'CloudServiceInfo',
        'ccsp_service': 'CcspServiceInfo',
        'vsm': 'VsmResourceInfo',
        'app': 'AppResourceInfo',
        'kms': 'KmsResourceInfo'
    }

    attribute_map = {
        'cloud_service': 'cloud_service',
        'ccsp_service': 'ccsp_service',
        'vsm': 'vsm',
        'app': 'app',
        'kms': 'kms'
    }

    def __init__(self, cloud_service=None, ccsp_service=None, vsm=None, app=None, kms=None):
        r"""ShowResourceInfoResponse

        The model defined in huaweicloud sdk

        :param cloud_service: 
        :type cloud_service: :class:`huaweicloudsdkcpcs.v1.CloudServiceInfo`
        :param ccsp_service: 
        :type ccsp_service: :class:`huaweicloudsdkcpcs.v1.CcspServiceInfo`
        :param vsm: 
        :type vsm: :class:`huaweicloudsdkcpcs.v1.VsmResourceInfo`
        :param app: 
        :type app: :class:`huaweicloudsdkcpcs.v1.AppResourceInfo`
        :param kms: 
        :type kms: :class:`huaweicloudsdkcpcs.v1.KmsResourceInfo`
        """
        
        super(ShowResourceInfoResponse, self).__init__()

        self._cloud_service = None
        self._ccsp_service = None
        self._vsm = None
        self._app = None
        self._kms = None
        self.discriminator = None

        if cloud_service is not None:
            self.cloud_service = cloud_service
        if ccsp_service is not None:
            self.ccsp_service = ccsp_service
        if vsm is not None:
            self.vsm = vsm
        if app is not None:
            self.app = app
        if kms is not None:
            self.kms = kms

    @property
    def cloud_service(self):
        r"""Gets the cloud_service of this ShowResourceInfoResponse.

        :return: The cloud_service of this ShowResourceInfoResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.CloudServiceInfo`
        """
        return self._cloud_service

    @cloud_service.setter
    def cloud_service(self, cloud_service):
        r"""Sets the cloud_service of this ShowResourceInfoResponse.

        :param cloud_service: The cloud_service of this ShowResourceInfoResponse.
        :type cloud_service: :class:`huaweicloudsdkcpcs.v1.CloudServiceInfo`
        """
        self._cloud_service = cloud_service

    @property
    def ccsp_service(self):
        r"""Gets the ccsp_service of this ShowResourceInfoResponse.

        :return: The ccsp_service of this ShowResourceInfoResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.CcspServiceInfo`
        """
        return self._ccsp_service

    @ccsp_service.setter
    def ccsp_service(self, ccsp_service):
        r"""Sets the ccsp_service of this ShowResourceInfoResponse.

        :param ccsp_service: The ccsp_service of this ShowResourceInfoResponse.
        :type ccsp_service: :class:`huaweicloudsdkcpcs.v1.CcspServiceInfo`
        """
        self._ccsp_service = ccsp_service

    @property
    def vsm(self):
        r"""Gets the vsm of this ShowResourceInfoResponse.

        :return: The vsm of this ShowResourceInfoResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.VsmResourceInfo`
        """
        return self._vsm

    @vsm.setter
    def vsm(self, vsm):
        r"""Sets the vsm of this ShowResourceInfoResponse.

        :param vsm: The vsm of this ShowResourceInfoResponse.
        :type vsm: :class:`huaweicloudsdkcpcs.v1.VsmResourceInfo`
        """
        self._vsm = vsm

    @property
    def app(self):
        r"""Gets the app of this ShowResourceInfoResponse.

        :return: The app of this ShowResourceInfoResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.AppResourceInfo`
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ShowResourceInfoResponse.

        :param app: The app of this ShowResourceInfoResponse.
        :type app: :class:`huaweicloudsdkcpcs.v1.AppResourceInfo`
        """
        self._app = app

    @property
    def kms(self):
        r"""Gets the kms of this ShowResourceInfoResponse.

        :return: The kms of this ShowResourceInfoResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.KmsResourceInfo`
        """
        return self._kms

    @kms.setter
    def kms(self, kms):
        r"""Sets the kms of this ShowResourceInfoResponse.

        :param kms: The kms of this ShowResourceInfoResponse.
        :type kms: :class:`huaweicloudsdkcpcs.v1.KmsResourceInfo`
        """
        self._kms = kms

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
        if not isinstance(other, ShowResourceInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
