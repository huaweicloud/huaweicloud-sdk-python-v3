# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackgroundInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'cover_file_name': 'str',
        'background_file_name': 'str',
        'logo_file_name': 'str'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'cover_file_name': 'cover_file_name',
        'background_file_name': 'background_file_name',
        'logo_file_name': 'logo_file_name'
    }

    def __init__(self, project_uuid=None, cover_file_name=None, background_file_name=None, logo_file_name=None):
        """ShowBackgroundInfoResponse

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param cover_file_name: cover文件名称
        :type cover_file_name: str
        :param background_file_name: 背景文件名称
        :type background_file_name: str
        :param logo_file_name: logo文件名称
        :type logo_file_name: str
        """
        
        super(ShowBackgroundInfoResponse, self).__init__()

        self._project_uuid = None
        self._cover_file_name = None
        self._background_file_name = None
        self._logo_file_name = None
        self.discriminator = None

        if project_uuid is not None:
            self.project_uuid = project_uuid
        if cover_file_name is not None:
            self.cover_file_name = cover_file_name
        if background_file_name is not None:
            self.background_file_name = background_file_name
        if logo_file_name is not None:
            self.logo_file_name = logo_file_name

    @property
    def project_uuid(self):
        """Gets the project_uuid of this ShowBackgroundInfoResponse.

        项目id

        :return: The project_uuid of this ShowBackgroundInfoResponse.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this ShowBackgroundInfoResponse.

        项目id

        :param project_uuid: The project_uuid of this ShowBackgroundInfoResponse.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def cover_file_name(self):
        """Gets the cover_file_name of this ShowBackgroundInfoResponse.

        cover文件名称

        :return: The cover_file_name of this ShowBackgroundInfoResponse.
        :rtype: str
        """
        return self._cover_file_name

    @cover_file_name.setter
    def cover_file_name(self, cover_file_name):
        """Sets the cover_file_name of this ShowBackgroundInfoResponse.

        cover文件名称

        :param cover_file_name: The cover_file_name of this ShowBackgroundInfoResponse.
        :type cover_file_name: str
        """
        self._cover_file_name = cover_file_name

    @property
    def background_file_name(self):
        """Gets the background_file_name of this ShowBackgroundInfoResponse.

        背景文件名称

        :return: The background_file_name of this ShowBackgroundInfoResponse.
        :rtype: str
        """
        return self._background_file_name

    @background_file_name.setter
    def background_file_name(self, background_file_name):
        """Sets the background_file_name of this ShowBackgroundInfoResponse.

        背景文件名称

        :param background_file_name: The background_file_name of this ShowBackgroundInfoResponse.
        :type background_file_name: str
        """
        self._background_file_name = background_file_name

    @property
    def logo_file_name(self):
        """Gets the logo_file_name of this ShowBackgroundInfoResponse.

        logo文件名称

        :return: The logo_file_name of this ShowBackgroundInfoResponse.
        :rtype: str
        """
        return self._logo_file_name

    @logo_file_name.setter
    def logo_file_name(self, logo_file_name):
        """Sets the logo_file_name of this ShowBackgroundInfoResponse.

        logo文件名称

        :param logo_file_name: The logo_file_name of this ShowBackgroundInfoResponse.
        :type logo_file_name: str
        """
        self._logo_file_name = logo_file_name

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
        if not isinstance(other, ShowBackgroundInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
