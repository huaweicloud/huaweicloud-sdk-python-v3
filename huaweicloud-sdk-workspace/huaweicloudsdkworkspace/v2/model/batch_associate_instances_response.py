# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAssociateInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assign_dimension': 'str',
        'desktop': 'list[DesktopDimensionAttachInfo]',
        'user': 'list[UserDimensionAttachInfo]',
        'desktops_attach_infos': 'list[AttachInstancesDesktopInfo]'
    }

    attribute_map = {
        'assign_dimension': 'assign_dimension',
        'desktop': 'desktop',
        'user': 'user',
        'desktops_attach_infos': 'desktops_attach_infos'
    }

    def __init__(self, assign_dimension=None, desktop=None, user=None, desktops_attach_infos=None):
        r"""BatchAssociateInstancesResponse

        The model defined in huaweicloud sdk

        :param assign_dimension: 分配的维度，当前支持“用户为维度”、“桌面为维度”两种。
        :type assign_dimension: str
        :param desktop: 桌面维度结果，如果assign_dimension为DEKSTOP，那么取这个结果。
        :type desktop: list[:class:`huaweicloudsdkworkspace.v2.DesktopDimensionAttachInfo`]
        :param user: 用户维度结果，如果assign_dimension为USER，那么取这个结果。
        :type user: list[:class:`huaweicloudsdkworkspace.v2.UserDimensionAttachInfo`]
        :param desktops_attach_infos: 桌面分配关系。
        :type desktops_attach_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        """
        
        super(BatchAssociateInstancesResponse, self).__init__()

        self._assign_dimension = None
        self._desktop = None
        self._user = None
        self._desktops_attach_infos = None
        self.discriminator = None

        if assign_dimension is not None:
            self.assign_dimension = assign_dimension
        if desktop is not None:
            self.desktop = desktop
        if user is not None:
            self.user = user
        if desktops_attach_infos is not None:
            self.desktops_attach_infos = desktops_attach_infos

    @property
    def assign_dimension(self):
        r"""Gets the assign_dimension of this BatchAssociateInstancesResponse.

        分配的维度，当前支持“用户为维度”、“桌面为维度”两种。

        :return: The assign_dimension of this BatchAssociateInstancesResponse.
        :rtype: str
        """
        return self._assign_dimension

    @assign_dimension.setter
    def assign_dimension(self, assign_dimension):
        r"""Sets the assign_dimension of this BatchAssociateInstancesResponse.

        分配的维度，当前支持“用户为维度”、“桌面为维度”两种。

        :param assign_dimension: The assign_dimension of this BatchAssociateInstancesResponse.
        :type assign_dimension: str
        """
        self._assign_dimension = assign_dimension

    @property
    def desktop(self):
        r"""Gets the desktop of this BatchAssociateInstancesResponse.

        桌面维度结果，如果assign_dimension为DEKSTOP，那么取这个结果。

        :return: The desktop of this BatchAssociateInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DesktopDimensionAttachInfo`]
        """
        return self._desktop

    @desktop.setter
    def desktop(self, desktop):
        r"""Sets the desktop of this BatchAssociateInstancesResponse.

        桌面维度结果，如果assign_dimension为DEKSTOP，那么取这个结果。

        :param desktop: The desktop of this BatchAssociateInstancesResponse.
        :type desktop: list[:class:`huaweicloudsdkworkspace.v2.DesktopDimensionAttachInfo`]
        """
        self._desktop = desktop

    @property
    def user(self):
        r"""Gets the user of this BatchAssociateInstancesResponse.

        用户维度结果，如果assign_dimension为USER，那么取这个结果。

        :return: The user of this BatchAssociateInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.UserDimensionAttachInfo`]
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this BatchAssociateInstancesResponse.

        用户维度结果，如果assign_dimension为USER，那么取这个结果。

        :param user: The user of this BatchAssociateInstancesResponse.
        :type user: list[:class:`huaweicloudsdkworkspace.v2.UserDimensionAttachInfo`]
        """
        self._user = user

    @property
    def desktops_attach_infos(self):
        r"""Gets the desktops_attach_infos of this BatchAssociateInstancesResponse.

        桌面分配关系。

        :return: The desktops_attach_infos of this BatchAssociateInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        """
        return self._desktops_attach_infos

    @desktops_attach_infos.setter
    def desktops_attach_infos(self, desktops_attach_infos):
        r"""Sets the desktops_attach_infos of this BatchAssociateInstancesResponse.

        桌面分配关系。

        :param desktops_attach_infos: The desktops_attach_infos of this BatchAssociateInstancesResponse.
        :type desktops_attach_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesDesktopInfo`]
        """
        self._desktops_attach_infos = desktops_attach_infos

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
        if not isinstance(other, BatchAssociateInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
