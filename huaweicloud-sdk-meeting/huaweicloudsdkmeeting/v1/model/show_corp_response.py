# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCorpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'QueryCorpBasicResultDTO',
        'admin_info': 'QueryAdminResultDTO',
        'res_info': 'QueryCorpResResultDTO',
        'group_dto': 'OrgGroupDTO',
        'id': 'str'
    }

    attribute_map = {
        'basic_info': 'basicInfo',
        'admin_info': 'adminInfo',
        'res_info': 'resInfo',
        'group_dto': 'groupDTO',
        'id': 'id'
    }

    def __init__(self, basic_info=None, admin_info=None, res_info=None, group_dto=None, id=None):
        r"""ShowCorpResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkmeeting.v1.QueryCorpBasicResultDTO`
        :param admin_info: 
        :type admin_info: :class:`huaweicloudsdkmeeting.v1.QueryAdminResultDTO`
        :param res_info: 
        :type res_info: :class:`huaweicloudsdkmeeting.v1.QueryCorpResResultDTO`
        :param group_dto: 
        :type group_dto: :class:`huaweicloudsdkmeeting.v1.OrgGroupDTO`
        :param id: 企业id。
        :type id: str
        """
        
        super(ShowCorpResponse, self).__init__()

        self._basic_info = None
        self._admin_info = None
        self._res_info = None
        self._group_dto = None
        self._id = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if admin_info is not None:
            self.admin_info = admin_info
        if res_info is not None:
            self.res_info = res_info
        if group_dto is not None:
            self.group_dto = group_dto
        if id is not None:
            self.id = id

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowCorpResponse.

        :return: The basic_info of this ShowCorpResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QueryCorpBasicResultDTO`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowCorpResponse.

        :param basic_info: The basic_info of this ShowCorpResponse.
        :type basic_info: :class:`huaweicloudsdkmeeting.v1.QueryCorpBasicResultDTO`
        """
        self._basic_info = basic_info

    @property
    def admin_info(self):
        r"""Gets the admin_info of this ShowCorpResponse.

        :return: The admin_info of this ShowCorpResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QueryAdminResultDTO`
        """
        return self._admin_info

    @admin_info.setter
    def admin_info(self, admin_info):
        r"""Sets the admin_info of this ShowCorpResponse.

        :param admin_info: The admin_info of this ShowCorpResponse.
        :type admin_info: :class:`huaweicloudsdkmeeting.v1.QueryAdminResultDTO`
        """
        self._admin_info = admin_info

    @property
    def res_info(self):
        r"""Gets the res_info of this ShowCorpResponse.

        :return: The res_info of this ShowCorpResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QueryCorpResResultDTO`
        """
        return self._res_info

    @res_info.setter
    def res_info(self, res_info):
        r"""Sets the res_info of this ShowCorpResponse.

        :param res_info: The res_info of this ShowCorpResponse.
        :type res_info: :class:`huaweicloudsdkmeeting.v1.QueryCorpResResultDTO`
        """
        self._res_info = res_info

    @property
    def group_dto(self):
        r"""Gets the group_dto of this ShowCorpResponse.

        :return: The group_dto of this ShowCorpResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.OrgGroupDTO`
        """
        return self._group_dto

    @group_dto.setter
    def group_dto(self, group_dto):
        r"""Sets the group_dto of this ShowCorpResponse.

        :param group_dto: The group_dto of this ShowCorpResponse.
        :type group_dto: :class:`huaweicloudsdkmeeting.v1.OrgGroupDTO`
        """
        self._group_dto = group_dto

    @property
    def id(self):
        r"""Gets the id of this ShowCorpResponse.

        企业id。

        :return: The id of this ShowCorpResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCorpResponse.

        企业id。

        :param id: The id of this ShowCorpResponse.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ShowCorpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
