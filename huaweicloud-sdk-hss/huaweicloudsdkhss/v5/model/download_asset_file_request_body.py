# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadAssetFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_param': 'str',
        'export_headers': 'list[list[str]]'
    }

    attribute_map = {
        'search_param': 'search_param',
        'export_headers': 'export_headers'
    }

    def __init__(self, search_param=None, export_headers=None):
        r"""DownloadAssetFileRequestBody

        The model defined in huaweicloud sdk

        :param search_param: **参数解释**: 查询条件，json格式字符串，如{\\\&quot;port_string\\\&quot;: \\\&quot;8080\\\&quot;} **约束限制**: 如下接口的请求参数的json格式 - users         ：/v5/{project_id}/asset/users - auto_launch   ：/v5/{project_id}/asset/auto-launchs - database      ：/v5/{project_id}/asset/web-app-and-services - jar_package   ：/v5/{project_id}/asset/midwares/detail - port          ：/v5/{project_id}/asset/ports/detail - process       ：/v5/{project_id}/asset/processes/detail - web_cms       ：/v5/{project_id}/asset/web-app-and-services - web_framework ：/v5/{project_id}/asset/host/web-framework - web_service   ：/v5/{project_id}/asset/web-app-and-services - web_site      ：/v5/{project_id}/asset/host/web-site - app           ：/v5/{project_id}/asset/apps - kernel_module ：/v5/{project_id}/asset/host/kernel-module  **取值范围**: 字符长度0-128 **默认取值**: 不涉及 
        :type search_param: str
        :param export_headers: **参数解释**: 导出数据表头信息详情 **约束限制**: 表头信息应为如下格式[[字段1,表头1显示名称],[字段2,表头2显示名称],[字段3,表头3显示名称]] **取值范围**: 可从如下取值中选取部分或全部组成表头信息 所有资产都有如下字段： - host_name：主机服务器名 - host_ip：主机ip 其他资产类别特有字段： - users   - user_name：用户名   - login_permission：是否有登陆权限   - root_permission：是否有root权限   - user_group_name：用户组   - user_home_dir：用户目录   - shell：用户启动shell   - recent_scan_time：最近扫描时间   - first_scan_time：首次扫描时间   - container_id：容器id   - container_name：容器名称 - auto_launch   - name：名称   - type：类型   - path：文件路径   - hash：文件hash   - run_user：运行用户   - recent_scan_time：最近扫描时间   - container_id：容器id   - container_name：容器名称 - database - web_cms - web_service   - name：软件名称   - version：软件版本   - install_path：安装路径   - config_path：配置文件路径   - uid：用户id   - mode：软件文件权限   - pid：软件进程id   - proc_path：软件进程路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - jar_package   - name：名称   - file_name：文件名   - catalogue：类别   - file_type：文件类型   - version：版本   - path：文件路径   - hash：文件hash   - uid：用户id   - gid：用户组id   - mode：文件权限   - pid：进程id   - proc_path：进程路径   - is_embedded：是否为内层jar包   - package_path：外层jar包路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - port   - port_status：端口是否需要处理   - port：端口号   - type：类型   - pid：进程ID   - path：程序文件路径   - laddr：监听的ip   - container_id：容器id   - container_name：容器名称 - process   - process_path：进程路径   - launch_params：启动参数   - launch_time：启动时间   - user_name：运行用户   - run_permission：运行权限   - process_pid：进程ID   - hash：文件hash   - container_id：容器id   - container_name：容器名称 - web_framework   - name：名称   - file_name：文件名   - catalogue：类别   - file_type：文件类型   - version：版本   - path：文件路径   - hash：文件hash   - uid：用户id   - gid：用户组id   - mode：文件权限   - pid：进程id   - proc_path：进程路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - web_site   - domain：对外域名   - port：对外端口号   - url_path：url路径   - path：web目录   - mode：web目录文件权限   - uid：用户id   - record_time：扫描时间   - is_https：是否为https   - pid：进程id   - cert_issuer：SSL证书颁发者   - cert_user：SSL证书使用者   - cert_issue_time：SSL证书颁发时间   - cert_expired_time：SSL证书到期时间   - container_id：容器id   - container_name：容器名称 - app   - app_name：软件名称   - version：版本号   - update_time：更新时间   - recent_scan_time：最近扫描时间   - container_id：容器id   - container_name：容器名称 - kernel_module   - name：名称   - version：版本   - srcversion：源码版本   - desc：描述   - path：文件路径   - size：文件大小   - mode：文件权限   - uid：用户id   - ctime：文件创建时间   - mtime：最后修改时间   - hash：文件hash   - record_time：扫描时间  **默认取值**: 不涉及 
        :type export_headers: list[list[str]]
        """
        
        

        self._search_param = None
        self._export_headers = None
        self.discriminator = None

        if search_param is not None:
            self.search_param = search_param
        self.export_headers = export_headers

    @property
    def search_param(self):
        r"""Gets the search_param of this DownloadAssetFileRequestBody.

        **参数解释**: 查询条件，json格式字符串，如{\\\"port_string\\\": \\\"8080\\\"} **约束限制**: 如下接口的请求参数的json格式 - users         ：/v5/{project_id}/asset/users - auto_launch   ：/v5/{project_id}/asset/auto-launchs - database      ：/v5/{project_id}/asset/web-app-and-services - jar_package   ：/v5/{project_id}/asset/midwares/detail - port          ：/v5/{project_id}/asset/ports/detail - process       ：/v5/{project_id}/asset/processes/detail - web_cms       ：/v5/{project_id}/asset/web-app-and-services - web_framework ：/v5/{project_id}/asset/host/web-framework - web_service   ：/v5/{project_id}/asset/web-app-and-services - web_site      ：/v5/{project_id}/asset/host/web-site - app           ：/v5/{project_id}/asset/apps - kernel_module ：/v5/{project_id}/asset/host/kernel-module  **取值范围**: 字符长度0-128 **默认取值**: 不涉及 

        :return: The search_param of this DownloadAssetFileRequestBody.
        :rtype: str
        """
        return self._search_param

    @search_param.setter
    def search_param(self, search_param):
        r"""Sets the search_param of this DownloadAssetFileRequestBody.

        **参数解释**: 查询条件，json格式字符串，如{\\\"port_string\\\": \\\"8080\\\"} **约束限制**: 如下接口的请求参数的json格式 - users         ：/v5/{project_id}/asset/users - auto_launch   ：/v5/{project_id}/asset/auto-launchs - database      ：/v5/{project_id}/asset/web-app-and-services - jar_package   ：/v5/{project_id}/asset/midwares/detail - port          ：/v5/{project_id}/asset/ports/detail - process       ：/v5/{project_id}/asset/processes/detail - web_cms       ：/v5/{project_id}/asset/web-app-and-services - web_framework ：/v5/{project_id}/asset/host/web-framework - web_service   ：/v5/{project_id}/asset/web-app-and-services - web_site      ：/v5/{project_id}/asset/host/web-site - app           ：/v5/{project_id}/asset/apps - kernel_module ：/v5/{project_id}/asset/host/kernel-module  **取值范围**: 字符长度0-128 **默认取值**: 不涉及 

        :param search_param: The search_param of this DownloadAssetFileRequestBody.
        :type search_param: str
        """
        self._search_param = search_param

    @property
    def export_headers(self):
        r"""Gets the export_headers of this DownloadAssetFileRequestBody.

        **参数解释**: 导出数据表头信息详情 **约束限制**: 表头信息应为如下格式[[字段1,表头1显示名称],[字段2,表头2显示名称],[字段3,表头3显示名称]] **取值范围**: 可从如下取值中选取部分或全部组成表头信息 所有资产都有如下字段： - host_name：主机服务器名 - host_ip：主机ip 其他资产类别特有字段： - users   - user_name：用户名   - login_permission：是否有登陆权限   - root_permission：是否有root权限   - user_group_name：用户组   - user_home_dir：用户目录   - shell：用户启动shell   - recent_scan_time：最近扫描时间   - first_scan_time：首次扫描时间   - container_id：容器id   - container_name：容器名称 - auto_launch   - name：名称   - type：类型   - path：文件路径   - hash：文件hash   - run_user：运行用户   - recent_scan_time：最近扫描时间   - container_id：容器id   - container_name：容器名称 - database - web_cms - web_service   - name：软件名称   - version：软件版本   - install_path：安装路径   - config_path：配置文件路径   - uid：用户id   - mode：软件文件权限   - pid：软件进程id   - proc_path：软件进程路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - jar_package   - name：名称   - file_name：文件名   - catalogue：类别   - file_type：文件类型   - version：版本   - path：文件路径   - hash：文件hash   - uid：用户id   - gid：用户组id   - mode：文件权限   - pid：进程id   - proc_path：进程路径   - is_embedded：是否为内层jar包   - package_path：外层jar包路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - port   - port_status：端口是否需要处理   - port：端口号   - type：类型   - pid：进程ID   - path：程序文件路径   - laddr：监听的ip   - container_id：容器id   - container_name：容器名称 - process   - process_path：进程路径   - launch_params：启动参数   - launch_time：启动时间   - user_name：运行用户   - run_permission：运行权限   - process_pid：进程ID   - hash：文件hash   - container_id：容器id   - container_name：容器名称 - web_framework   - name：名称   - file_name：文件名   - catalogue：类别   - file_type：文件类型   - version：版本   - path：文件路径   - hash：文件hash   - uid：用户id   - gid：用户组id   - mode：文件权限   - pid：进程id   - proc_path：进程路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - web_site   - domain：对外域名   - port：对外端口号   - url_path：url路径   - path：web目录   - mode：web目录文件权限   - uid：用户id   - record_time：扫描时间   - is_https：是否为https   - pid：进程id   - cert_issuer：SSL证书颁发者   - cert_user：SSL证书使用者   - cert_issue_time：SSL证书颁发时间   - cert_expired_time：SSL证书到期时间   - container_id：容器id   - container_name：容器名称 - app   - app_name：软件名称   - version：版本号   - update_time：更新时间   - recent_scan_time：最近扫描时间   - container_id：容器id   - container_name：容器名称 - kernel_module   - name：名称   - version：版本   - srcversion：源码版本   - desc：描述   - path：文件路径   - size：文件大小   - mode：文件权限   - uid：用户id   - ctime：文件创建时间   - mtime：最后修改时间   - hash：文件hash   - record_time：扫描时间  **默认取值**: 不涉及 

        :return: The export_headers of this DownloadAssetFileRequestBody.
        :rtype: list[list[str]]
        """
        return self._export_headers

    @export_headers.setter
    def export_headers(self, export_headers):
        r"""Sets the export_headers of this DownloadAssetFileRequestBody.

        **参数解释**: 导出数据表头信息详情 **约束限制**: 表头信息应为如下格式[[字段1,表头1显示名称],[字段2,表头2显示名称],[字段3,表头3显示名称]] **取值范围**: 可从如下取值中选取部分或全部组成表头信息 所有资产都有如下字段： - host_name：主机服务器名 - host_ip：主机ip 其他资产类别特有字段： - users   - user_name：用户名   - login_permission：是否有登陆权限   - root_permission：是否有root权限   - user_group_name：用户组   - user_home_dir：用户目录   - shell：用户启动shell   - recent_scan_time：最近扫描时间   - first_scan_time：首次扫描时间   - container_id：容器id   - container_name：容器名称 - auto_launch   - name：名称   - type：类型   - path：文件路径   - hash：文件hash   - run_user：运行用户   - recent_scan_time：最近扫描时间   - container_id：容器id   - container_name：容器名称 - database - web_cms - web_service   - name：软件名称   - version：软件版本   - install_path：安装路径   - config_path：配置文件路径   - uid：用户id   - mode：软件文件权限   - pid：软件进程id   - proc_path：软件进程路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - jar_package   - name：名称   - file_name：文件名   - catalogue：类别   - file_type：文件类型   - version：版本   - path：文件路径   - hash：文件hash   - uid：用户id   - gid：用户组id   - mode：文件权限   - pid：进程id   - proc_path：进程路径   - is_embedded：是否为内层jar包   - package_path：外层jar包路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - port   - port_status：端口是否需要处理   - port：端口号   - type：类型   - pid：进程ID   - path：程序文件路径   - laddr：监听的ip   - container_id：容器id   - container_name：容器名称 - process   - process_path：进程路径   - launch_params：启动参数   - launch_time：启动时间   - user_name：运行用户   - run_permission：运行权限   - process_pid：进程ID   - hash：文件hash   - container_id：容器id   - container_name：容器名称 - web_framework   - name：名称   - file_name：文件名   - catalogue：类别   - file_type：文件类型   - version：版本   - path：文件路径   - hash：文件hash   - uid：用户id   - gid：用户组id   - mode：文件权限   - pid：进程id   - proc_path：进程路径   - record_time：扫描时间   - container_id：容器id   - container_name：容器名称 - web_site   - domain：对外域名   - port：对外端口号   - url_path：url路径   - path：web目录   - mode：web目录文件权限   - uid：用户id   - record_time：扫描时间   - is_https：是否为https   - pid：进程id   - cert_issuer：SSL证书颁发者   - cert_user：SSL证书使用者   - cert_issue_time：SSL证书颁发时间   - cert_expired_time：SSL证书到期时间   - container_id：容器id   - container_name：容器名称 - app   - app_name：软件名称   - version：版本号   - update_time：更新时间   - recent_scan_time：最近扫描时间   - container_id：容器id   - container_name：容器名称 - kernel_module   - name：名称   - version：版本   - srcversion：源码版本   - desc：描述   - path：文件路径   - size：文件大小   - mode：文件权限   - uid：用户id   - ctime：文件创建时间   - mtime：最后修改时间   - hash：文件hash   - record_time：扫描时间  **默认取值**: 不涉及 

        :param export_headers: The export_headers of this DownloadAssetFileRequestBody.
        :type export_headers: list[list[str]]
        """
        self._export_headers = export_headers

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
        if not isinstance(other, DownloadAssetFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
