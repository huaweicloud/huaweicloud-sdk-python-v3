# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeProtectedInstanceRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'production_flavor_ref': 'str',
        'dr_flavor_ref': 'str',
        'production_dedicated_host_id': 'str',
        'dr_dedicated_host_id': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef',
        'production_flavor_ref': 'production_flavorRef',
        'dr_flavor_ref': 'dr_flavorRef',
        'production_dedicated_host_id': 'production_dedicated_host_id',
        'dr_dedicated_host_id': 'dr_dedicated_host_id'
    }

    def __init__(self, flavor_ref=None, production_flavor_ref=None, dr_flavor_ref=None, production_dedicated_host_id=None, dr_dedicated_host_id=None):
        """ResizeProtectedInstanceRequestParams

        The model defined in huaweicloud sdk

        :param flavor_ref: 变更规格后，生产站点云服务器和容灾站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持同时变更生产站点云服务器和容灾站点云服务器的规格。如需同时变更，请使用flavorRef参数，变更规格后，生产站点云服务器和容灾站点云服务器的规格相同。
        :type flavor_ref: str
        :param production_flavor_ref: 变更规格后，生产站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持仅变更生产站点云服务器的规格。此时，请使用production_flavorRef参数。当flavorRef参数有值时，production_flavorRef参数不生效。
        :type production_flavor_ref: str
        :param dr_flavor_ref: 变更规格后，容灾站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持仅变更容灾站点云服务器的规格。此时，请使用dr_flavorRef参数。当flavorRef参数有值时，dr_flavorRef参数不生效。
        :type dr_flavor_ref: str
        :param production_dedicated_host_id: 新生产站点专属主机ID。 说明：生产站点云服务器在专属主机上时，变更规格需要指定此参数。可以指定为生产站点云服务器当前所在专属主机ID或其他专属主机ID。
        :type production_dedicated_host_id: str
        :param dr_dedicated_host_id: 新容灾站点专属主机ID。 说明：容灾站点云服务器在专属主机上时，变更规格需要指定此参数。可以指定为容灾站点云服务器当前所在专属主机ID或其他专属主机ID。
        :type dr_dedicated_host_id: str
        """
        
        

        self._flavor_ref = None
        self._production_flavor_ref = None
        self._dr_flavor_ref = None
        self._production_dedicated_host_id = None
        self._dr_dedicated_host_id = None
        self.discriminator = None

        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if production_flavor_ref is not None:
            self.production_flavor_ref = production_flavor_ref
        if dr_flavor_ref is not None:
            self.dr_flavor_ref = dr_flavor_ref
        if production_dedicated_host_id is not None:
            self.production_dedicated_host_id = production_dedicated_host_id
        if dr_dedicated_host_id is not None:
            self.dr_dedicated_host_id = dr_dedicated_host_id

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this ResizeProtectedInstanceRequestParams.

        变更规格后，生产站点云服务器和容灾站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持同时变更生产站点云服务器和容灾站点云服务器的规格。如需同时变更，请使用flavorRef参数，变更规格后，生产站点云服务器和容灾站点云服务器的规格相同。

        :return: The flavor_ref of this ResizeProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this ResizeProtectedInstanceRequestParams.

        变更规格后，生产站点云服务器和容灾站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持同时变更生产站点云服务器和容灾站点云服务器的规格。如需同时变更，请使用flavorRef参数，变更规格后，生产站点云服务器和容灾站点云服务器的规格相同。

        :param flavor_ref: The flavor_ref of this ResizeProtectedInstanceRequestParams.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def production_flavor_ref(self):
        """Gets the production_flavor_ref of this ResizeProtectedInstanceRequestParams.

        变更规格后，生产站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持仅变更生产站点云服务器的规格。此时，请使用production_flavorRef参数。当flavorRef参数有值时，production_flavorRef参数不生效。

        :return: The production_flavor_ref of this ResizeProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._production_flavor_ref

    @production_flavor_ref.setter
    def production_flavor_ref(self, production_flavor_ref):
        """Sets the production_flavor_ref of this ResizeProtectedInstanceRequestParams.

        变更规格后，生产站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持仅变更生产站点云服务器的规格。此时，请使用production_flavorRef参数。当flavorRef参数有值时，production_flavorRef参数不生效。

        :param production_flavor_ref: The production_flavor_ref of this ResizeProtectedInstanceRequestParams.
        :type production_flavor_ref: str
        """
        self._production_flavor_ref = production_flavor_ref

    @property
    def dr_flavor_ref(self):
        """Gets the dr_flavor_ref of this ResizeProtectedInstanceRequestParams.

        变更规格后，容灾站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持仅变更容灾站点云服务器的规格。此时，请使用dr_flavorRef参数。当flavorRef参数有值时，dr_flavorRef参数不生效。

        :return: The dr_flavor_ref of this ResizeProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._dr_flavor_ref

    @dr_flavor_ref.setter
    def dr_flavor_ref(self, dr_flavor_ref):
        """Sets the dr_flavor_ref of this ResizeProtectedInstanceRequestParams.

        变更规格后，容灾站点云服务器的flavor ID。可通过查询云服务器规格变更支持列表接口获取。 说明：系统支持仅变更容灾站点云服务器的规格。此时，请使用dr_flavorRef参数。当flavorRef参数有值时，dr_flavorRef参数不生效。

        :param dr_flavor_ref: The dr_flavor_ref of this ResizeProtectedInstanceRequestParams.
        :type dr_flavor_ref: str
        """
        self._dr_flavor_ref = dr_flavor_ref

    @property
    def production_dedicated_host_id(self):
        """Gets the production_dedicated_host_id of this ResizeProtectedInstanceRequestParams.

        新生产站点专属主机ID。 说明：生产站点云服务器在专属主机上时，变更规格需要指定此参数。可以指定为生产站点云服务器当前所在专属主机ID或其他专属主机ID。

        :return: The production_dedicated_host_id of this ResizeProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._production_dedicated_host_id

    @production_dedicated_host_id.setter
    def production_dedicated_host_id(self, production_dedicated_host_id):
        """Sets the production_dedicated_host_id of this ResizeProtectedInstanceRequestParams.

        新生产站点专属主机ID。 说明：生产站点云服务器在专属主机上时，变更规格需要指定此参数。可以指定为生产站点云服务器当前所在专属主机ID或其他专属主机ID。

        :param production_dedicated_host_id: The production_dedicated_host_id of this ResizeProtectedInstanceRequestParams.
        :type production_dedicated_host_id: str
        """
        self._production_dedicated_host_id = production_dedicated_host_id

    @property
    def dr_dedicated_host_id(self):
        """Gets the dr_dedicated_host_id of this ResizeProtectedInstanceRequestParams.

        新容灾站点专属主机ID。 说明：容灾站点云服务器在专属主机上时，变更规格需要指定此参数。可以指定为容灾站点云服务器当前所在专属主机ID或其他专属主机ID。

        :return: The dr_dedicated_host_id of this ResizeProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._dr_dedicated_host_id

    @dr_dedicated_host_id.setter
    def dr_dedicated_host_id(self, dr_dedicated_host_id):
        """Sets the dr_dedicated_host_id of this ResizeProtectedInstanceRequestParams.

        新容灾站点专属主机ID。 说明：容灾站点云服务器在专属主机上时，变更规格需要指定此参数。可以指定为容灾站点云服务器当前所在专属主机ID或其他专属主机ID。

        :param dr_dedicated_host_id: The dr_dedicated_host_id of this ResizeProtectedInstanceRequestParams.
        :type dr_dedicated_host_id: str
        """
        self._dr_dedicated_host_id = dr_dedicated_host_id

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
        if not isinstance(other, ResizeProtectedInstanceRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
