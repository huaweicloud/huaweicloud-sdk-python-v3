# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSloDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'application_name': 'str',
        'application_id': 'str',
        'slo_targets': 'float',
        'sli_list': 'list[SliDetail]'
    }

    attribute_map = {
        'id': 'id',
        'application_name': 'application_name',
        'application_id': 'application_id',
        'slo_targets': 'slo_targets',
        'sli_list': 'sli_list'
    }

    def __init__(self, id=None, application_name=None, application_id=None, slo_targets=None, sli_list=None):
        r"""ShowSloDetailResponse

        The model defined in huaweicloud sdk

        :param id: SLO的ID
        :type id: str
        :param application_name: 应用名称
        :type application_name: str
        :param application_id: 应用ID
        :type application_id: str
        :param slo_targets: SLO的目标值
        :type slo_targets: float
        :param sli_list: SLi列表
        :type sli_list: list[:class:`huaweicloudsdkcoc.v1.SliDetail`]
        """
        
        super(ShowSloDetailResponse, self).__init__()

        self._id = None
        self._application_name = None
        self._application_id = None
        self._slo_targets = None
        self._sli_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application_name is not None:
            self.application_name = application_name
        if application_id is not None:
            self.application_id = application_id
        if slo_targets is not None:
            self.slo_targets = slo_targets
        if sli_list is not None:
            self.sli_list = sli_list

    @property
    def id(self):
        r"""Gets the id of this ShowSloDetailResponse.

        SLO的ID

        :return: The id of this ShowSloDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowSloDetailResponse.

        SLO的ID

        :param id: The id of this ShowSloDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def application_name(self):
        r"""Gets the application_name of this ShowSloDetailResponse.

        应用名称

        :return: The application_name of this ShowSloDetailResponse.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this ShowSloDetailResponse.

        应用名称

        :param application_name: The application_name of this ShowSloDetailResponse.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def application_id(self):
        r"""Gets the application_id of this ShowSloDetailResponse.

        应用ID

        :return: The application_id of this ShowSloDetailResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ShowSloDetailResponse.

        应用ID

        :param application_id: The application_id of this ShowSloDetailResponse.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def slo_targets(self):
        r"""Gets the slo_targets of this ShowSloDetailResponse.

        SLO的目标值

        :return: The slo_targets of this ShowSloDetailResponse.
        :rtype: float
        """
        return self._slo_targets

    @slo_targets.setter
    def slo_targets(self, slo_targets):
        r"""Sets the slo_targets of this ShowSloDetailResponse.

        SLO的目标值

        :param slo_targets: The slo_targets of this ShowSloDetailResponse.
        :type slo_targets: float
        """
        self._slo_targets = slo_targets

    @property
    def sli_list(self):
        r"""Gets the sli_list of this ShowSloDetailResponse.

        SLi列表

        :return: The sli_list of this ShowSloDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.SliDetail`]
        """
        return self._sli_list

    @sli_list.setter
    def sli_list(self, sli_list):
        r"""Sets the sli_list of this ShowSloDetailResponse.

        SLi列表

        :param sli_list: The sli_list of this ShowSloDetailResponse.
        :type sli_list: list[:class:`huaweicloudsdkcoc.v1.SliDetail`]
        """
        self._sli_list = sli_list

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
        if not isinstance(other, ShowSloDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
