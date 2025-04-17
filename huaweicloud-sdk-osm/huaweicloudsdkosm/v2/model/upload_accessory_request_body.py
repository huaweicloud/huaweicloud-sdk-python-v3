# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAccessoryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file',
        'form_data': 'str'
    }

    attribute_map = {
        'file': 'file',
        'form_data': 'form_data'
    }

    def __init__(self, file=None, form_data=None):
        r"""UploadAccessoryRequestBody

        The model defined in huaweicloud sdk

        :param file: 文件内容
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param form_data: 附件的一些信息，比如来源
        :type form_data: str
        """
        
        

        self._file = None
        self._form_data = None
        self.discriminator = None

        self.file = file
        self.form_data = form_data

    @property
    def file(self):
        r"""Gets the file of this UploadAccessoryRequestBody.

        文件内容

        :return: The file of this UploadAccessoryRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this UploadAccessoryRequestBody.

        文件内容

        :param file: The file of this UploadAccessoryRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def form_data(self):
        r"""Gets the form_data of this UploadAccessoryRequestBody.

        附件的一些信息，比如来源

        :return: The form_data of this UploadAccessoryRequestBody.
        :rtype: str
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        r"""Sets the form_data of this UploadAccessoryRequestBody.

        附件的一些信息，比如来源

        :param form_data: The form_data of this UploadAccessoryRequestBody.
        :type form_data: str
        """
        self._form_data = form_data

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
        if not isinstance(other, UploadAccessoryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
