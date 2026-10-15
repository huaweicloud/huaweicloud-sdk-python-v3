# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportReportObsTmpFileUrlResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'obs_temp_uri': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'obs_temp_uri': 'obs_temp_uri'
    }

    def __init__(self, file_name=None, obs_temp_uri=None):
        r"""ExportReportObsTmpFileUrlResp

        The model defined in huaweicloud sdk

        :param file_name: 文件名
        :type file_name: str
        :param obs_temp_uri: OBS文件临时URI
        :type obs_temp_uri: str
        """
        
        

        self._file_name = None
        self._obs_temp_uri = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if obs_temp_uri is not None:
            self.obs_temp_uri = obs_temp_uri

    @property
    def file_name(self):
        r"""Gets the file_name of this ExportReportObsTmpFileUrlResp.

        文件名

        :return: The file_name of this ExportReportObsTmpFileUrlResp.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ExportReportObsTmpFileUrlResp.

        文件名

        :param file_name: The file_name of this ExportReportObsTmpFileUrlResp.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def obs_temp_uri(self):
        r"""Gets the obs_temp_uri of this ExportReportObsTmpFileUrlResp.

        OBS文件临时URI

        :return: The obs_temp_uri of this ExportReportObsTmpFileUrlResp.
        :rtype: str
        """
        return self._obs_temp_uri

    @obs_temp_uri.setter
    def obs_temp_uri(self, obs_temp_uri):
        r"""Sets the obs_temp_uri of this ExportReportObsTmpFileUrlResp.

        OBS文件临时URI

        :param obs_temp_uri: The obs_temp_uri of this ExportReportObsTmpFileUrlResp.
        :type obs_temp_uri: str
        """
        self._obs_temp_uri = obs_temp_uri

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
        if not isinstance(other, ExportReportObsTmpFileUrlResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
