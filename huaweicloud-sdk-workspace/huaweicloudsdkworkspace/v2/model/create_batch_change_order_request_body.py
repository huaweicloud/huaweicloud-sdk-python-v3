# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBatchChangeOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'add_volume_param': 'EstimateAddVolumeRequestBody',
        'extend_volume_param': 'EstimateExtendVolumeRequestBody',
        'resize_param': 'CreateResizeOrderRequestBody',
        'change_image_param': 'CreateChangeImageOrderRequestBody',
        'add_sub_resources_param': 'EstimateAddSubResourcesRequestBody',
        'delete_sub_resources_param': 'CreateDeleteSubResourcesOrderRequestBody'
    }

    attribute_map = {
        'type': 'type',
        'add_volume_param': 'add_volume_param',
        'extend_volume_param': 'extend_volume_param',
        'resize_param': 'resize_param',
        'change_image_param': 'change_image_param',
        'add_sub_resources_param': 'add_sub_resources_param',
        'delete_sub_resources_param': 'delete_sub_resources_param'
    }

    def __init__(self, type=None, add_volume_param=None, extend_volume_param=None, resize_param=None, change_image_param=None, add_sub_resources_param=None, delete_sub_resources_param=None):
        r"""CreateBatchChangeOrderRequestBody

        The model defined in huaweicloud sdk

        :param type: 下单类型。  - ADD_VOLUME：增加磁盘  - EXTEND_VOLUME：扩容磁盘  - RESIZE：变更规格  - CHANGE_IMAGE：切换镜像  - ADD_SUB_RESOURCES：购买桌面协同资源  - DELETE_SUB_RESOURCES：退订桌面协同资源
        :type type: str
        :param add_volume_param: 
        :type add_volume_param: :class:`huaweicloudsdkworkspace.v2.EstimateAddVolumeRequestBody`
        :param extend_volume_param: 
        :type extend_volume_param: :class:`huaweicloudsdkworkspace.v2.EstimateExtendVolumeRequestBody`
        :param resize_param: 
        :type resize_param: :class:`huaweicloudsdkworkspace.v2.CreateResizeOrderRequestBody`
        :param change_image_param: 
        :type change_image_param: :class:`huaweicloudsdkworkspace.v2.CreateChangeImageOrderRequestBody`
        :param add_sub_resources_param: 
        :type add_sub_resources_param: :class:`huaweicloudsdkworkspace.v2.EstimateAddSubResourcesRequestBody`
        :param delete_sub_resources_param: 
        :type delete_sub_resources_param: :class:`huaweicloudsdkworkspace.v2.CreateDeleteSubResourcesOrderRequestBody`
        """
        
        

        self._type = None
        self._add_volume_param = None
        self._extend_volume_param = None
        self._resize_param = None
        self._change_image_param = None
        self._add_sub_resources_param = None
        self._delete_sub_resources_param = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if add_volume_param is not None:
            self.add_volume_param = add_volume_param
        if extend_volume_param is not None:
            self.extend_volume_param = extend_volume_param
        if resize_param is not None:
            self.resize_param = resize_param
        if change_image_param is not None:
            self.change_image_param = change_image_param
        if add_sub_resources_param is not None:
            self.add_sub_resources_param = add_sub_resources_param
        if delete_sub_resources_param is not None:
            self.delete_sub_resources_param = delete_sub_resources_param

    @property
    def type(self):
        r"""Gets the type of this CreateBatchChangeOrderRequestBody.

        下单类型。  - ADD_VOLUME：增加磁盘  - EXTEND_VOLUME：扩容磁盘  - RESIZE：变更规格  - CHANGE_IMAGE：切换镜像  - ADD_SUB_RESOURCES：购买桌面协同资源  - DELETE_SUB_RESOURCES：退订桌面协同资源

        :return: The type of this CreateBatchChangeOrderRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateBatchChangeOrderRequestBody.

        下单类型。  - ADD_VOLUME：增加磁盘  - EXTEND_VOLUME：扩容磁盘  - RESIZE：变更规格  - CHANGE_IMAGE：切换镜像  - ADD_SUB_RESOURCES：购买桌面协同资源  - DELETE_SUB_RESOURCES：退订桌面协同资源

        :param type: The type of this CreateBatchChangeOrderRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def add_volume_param(self):
        r"""Gets the add_volume_param of this CreateBatchChangeOrderRequestBody.

        :return: The add_volume_param of this CreateBatchChangeOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateAddVolumeRequestBody`
        """
        return self._add_volume_param

    @add_volume_param.setter
    def add_volume_param(self, add_volume_param):
        r"""Sets the add_volume_param of this CreateBatchChangeOrderRequestBody.

        :param add_volume_param: The add_volume_param of this CreateBatchChangeOrderRequestBody.
        :type add_volume_param: :class:`huaweicloudsdkworkspace.v2.EstimateAddVolumeRequestBody`
        """
        self._add_volume_param = add_volume_param

    @property
    def extend_volume_param(self):
        r"""Gets the extend_volume_param of this CreateBatchChangeOrderRequestBody.

        :return: The extend_volume_param of this CreateBatchChangeOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateExtendVolumeRequestBody`
        """
        return self._extend_volume_param

    @extend_volume_param.setter
    def extend_volume_param(self, extend_volume_param):
        r"""Sets the extend_volume_param of this CreateBatchChangeOrderRequestBody.

        :param extend_volume_param: The extend_volume_param of this CreateBatchChangeOrderRequestBody.
        :type extend_volume_param: :class:`huaweicloudsdkworkspace.v2.EstimateExtendVolumeRequestBody`
        """
        self._extend_volume_param = extend_volume_param

    @property
    def resize_param(self):
        r"""Gets the resize_param of this CreateBatchChangeOrderRequestBody.

        :return: The resize_param of this CreateBatchChangeOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateResizeOrderRequestBody`
        """
        return self._resize_param

    @resize_param.setter
    def resize_param(self, resize_param):
        r"""Sets the resize_param of this CreateBatchChangeOrderRequestBody.

        :param resize_param: The resize_param of this CreateBatchChangeOrderRequestBody.
        :type resize_param: :class:`huaweicloudsdkworkspace.v2.CreateResizeOrderRequestBody`
        """
        self._resize_param = resize_param

    @property
    def change_image_param(self):
        r"""Gets the change_image_param of this CreateBatchChangeOrderRequestBody.

        :return: The change_image_param of this CreateBatchChangeOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateChangeImageOrderRequestBody`
        """
        return self._change_image_param

    @change_image_param.setter
    def change_image_param(self, change_image_param):
        r"""Sets the change_image_param of this CreateBatchChangeOrderRequestBody.

        :param change_image_param: The change_image_param of this CreateBatchChangeOrderRequestBody.
        :type change_image_param: :class:`huaweicloudsdkworkspace.v2.CreateChangeImageOrderRequestBody`
        """
        self._change_image_param = change_image_param

    @property
    def add_sub_resources_param(self):
        r"""Gets the add_sub_resources_param of this CreateBatchChangeOrderRequestBody.

        :return: The add_sub_resources_param of this CreateBatchChangeOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.EstimateAddSubResourcesRequestBody`
        """
        return self._add_sub_resources_param

    @add_sub_resources_param.setter
    def add_sub_resources_param(self, add_sub_resources_param):
        r"""Sets the add_sub_resources_param of this CreateBatchChangeOrderRequestBody.

        :param add_sub_resources_param: The add_sub_resources_param of this CreateBatchChangeOrderRequestBody.
        :type add_sub_resources_param: :class:`huaweicloudsdkworkspace.v2.EstimateAddSubResourcesRequestBody`
        """
        self._add_sub_resources_param = add_sub_resources_param

    @property
    def delete_sub_resources_param(self):
        r"""Gets the delete_sub_resources_param of this CreateBatchChangeOrderRequestBody.

        :return: The delete_sub_resources_param of this CreateBatchChangeOrderRequestBody.
        :rtype: :class:`huaweicloudsdkworkspace.v2.CreateDeleteSubResourcesOrderRequestBody`
        """
        return self._delete_sub_resources_param

    @delete_sub_resources_param.setter
    def delete_sub_resources_param(self, delete_sub_resources_param):
        r"""Sets the delete_sub_resources_param of this CreateBatchChangeOrderRequestBody.

        :param delete_sub_resources_param: The delete_sub_resources_param of this CreateBatchChangeOrderRequestBody.
        :type delete_sub_resources_param: :class:`huaweicloudsdkworkspace.v2.CreateDeleteSubResourcesOrderRequestBody`
        """
        self._delete_sub_resources_param = delete_sub_resources_param

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
        if not isinstance(other, CreateBatchChangeOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
