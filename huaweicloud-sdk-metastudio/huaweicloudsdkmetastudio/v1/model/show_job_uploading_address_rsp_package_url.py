# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobUploadingAddressRspPackageUrl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'training_data_uploading_url': 'str'
    }

    attribute_map = {
        'training_data_uploading_url': 'training_data_uploading_url'
    }

    def __init__(self, training_data_uploading_url=None):
        r"""ShowJobUploadingAddressRspPackageUrl

        The model defined in huaweicloud sdk

        :param training_data_uploading_url: 上传的训练数据地址,用户需要将训练数据打成zip包后上传到该url。 &gt; * 通过该obs地址上传时需要设置content-type为application/zip
        :type training_data_uploading_url: str
        """
        
        

        self._training_data_uploading_url = None
        self.discriminator = None

        if training_data_uploading_url is not None:
            self.training_data_uploading_url = training_data_uploading_url

    @property
    def training_data_uploading_url(self):
        r"""Gets the training_data_uploading_url of this ShowJobUploadingAddressRspPackageUrl.

        上传的训练数据地址,用户需要将训练数据打成zip包后上传到该url。 > * 通过该obs地址上传时需要设置content-type为application/zip

        :return: The training_data_uploading_url of this ShowJobUploadingAddressRspPackageUrl.
        :rtype: str
        """
        return self._training_data_uploading_url

    @training_data_uploading_url.setter
    def training_data_uploading_url(self, training_data_uploading_url):
        r"""Sets the training_data_uploading_url of this ShowJobUploadingAddressRspPackageUrl.

        上传的训练数据地址,用户需要将训练数据打成zip包后上传到该url。 > * 通过该obs地址上传时需要设置content-type为application/zip

        :param training_data_uploading_url: The training_data_uploading_url of this ShowJobUploadingAddressRspPackageUrl.
        :type training_data_uploading_url: str
        """
        self._training_data_uploading_url = training_data_uploading_url

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
        if not isinstance(other, ShowJobUploadingAddressRspPackageUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
